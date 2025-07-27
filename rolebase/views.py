from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializer import UserSerializer, RegisterSerializer
from .permission import HasRole
from .utils import required_role
from django.contrib.auth.models import User
from .models import UserRole, Role, ManageUser

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
# @required_role('Admin', 'Manager')

def user_list_view(request):
    user_role = UserRole.objects.get(user=request.user)
    if user_role.role.name == 'Admin':
        query = User.objects.all()
    elif user_role.role.name == 'Manager':
        managed_user_ids = ManageUser.objects.filter(manager=request.user).values_list('user_id', flat=True)
        query = User.objects.filter(id__in=managed_user_ids)
    else:
         return Response({'error': 'Not authorized to view user list'}, status=403)
    
    serializer = UserSerializer(query, many=True)
    return Response({
        'data' : serializer.data,
    }, status=201)

@api_view(['POST'])
def custome_login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(request, username=username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        token = refresh.access_token
        serializer = UserSerializer(user)

        return Response({
            'refresh': str(refresh),
            'access': str(token),
            'user': serializer.data
        }, status=201)
    else:
        return Response({
            'message': 'Invalid Username & Password !!!'
        })
    

@api_view(['POST'])
def register_view(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'data': serializer.data,
                'message': 'User created successfully'  
            }, status=201)
        else:
            return Response({
                'data': serializer.errors,
                'message': 'User creation failed'
            }, status=400)
    else:
        return Response({
            'message': 'GET Method not allowed'
        }, status=405)
