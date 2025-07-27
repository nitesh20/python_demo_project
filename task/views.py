from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializer import TaskSerializer
from .models import Task
from rolebase.models import UserRole

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def task_list_view(request):
    user_role = UserRole.objects.get(user=request.user)
    # if user_role.role.name == 'Admin':
    #     query = Task.objects.all()
    if user_role.role.name == 'Manager':
        query = Task.objects.filter(assigned_by=request.user)
    elif user_role.role.name == 'User':
        query = Task.objects.filter(assigned_to=request.user)
    else:
        return Response({'error': 'Not authorized to view task list'}, status=403)

    serializer = TaskSerializer(query, many=True)
    return Response({
        'data' : serializer.data,
    }, status=201)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_task_view(request):
    user_role = UserRole.objects.get(user=request.user)

    if (user_role.role.name == 'Admin') or (user_role.role.name == 'Manager'):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(assigned_by=request.user)
            return Response({
                'data' : serializer.data,
                'message' : 'Task Added Successfully.'
            }, status=201)
        else:
            return Response({
                'error': serializer.errors,
                'message': 'Something went wrong !!'
            }, status=400)
    else:
        return Response({'error': 'Not authorized to add task'}, status=403)    
    
@api_view(['GET']) 
@permission_classes([IsAuthenticated])   
def show_task_view(request, id):
    query = Task.objects.id(id=id)
    if query is not None: 
      serializer  = TaskSerializer(query, data=request.data)
      return Response({
          'data': serializer.data
      }, status=201)
    else:
        return Response({
            'message': 'Record not found'
        }, status=400)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_task_view(request, id):
    user_role = UserRole.objects.get(user=request.user)
    if (user_role.role.name == 'Manager') or (user_role.role.name == 'User'):
        query = Task.objects.get(id=id)
        if query is not None:
            serializer = TaskSerializer(query, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'data': serializer.data,
                    'message': 'Record updated successfully'
                }, status=201)
        else:
            return Response({
                'message': 'Record not found'
            }, status=400)
    else:
       return Response({'error': 'Not authorized to update task'}, status=403)  
    

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_task_view(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response({'message': 'Task not found'})

    task.delete()
    return Response({'message': 'Task deleted successfully'})

