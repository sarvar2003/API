from rest_framework import serializers

from core import models


class TaskSerializer(serializers.ModelSerializer):
    """Serializer class for task model"""

    class Meta:
        model = models.Task
        fields = ('id', 'title', 'task', 'date_created')
        read_only_fields = ('id', 'date_created')

class TaskDetailSerializer(TaskSerializer):
    """Serializer for task detail"""