from rest_framework import mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Task

from . import serializers


class TaskListViewset(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage tasks in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)
    
