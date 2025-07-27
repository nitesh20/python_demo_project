from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    assigned_to_name = serializers.CharField(source='assigned_to.username', read_only=True)
    assigned_by_name = serializers.CharField(source='assigned_by.username', read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'title', 'assigned_to', 'assigned_to_name', 'assigned_by', 'assigned_by_name', 'created_at']
        read_only_fields = ['assigned_by']

            