from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core.models import Task
from to_do_list.serializers import TaskSerializer

TASK_URL = reverse('to_do_list:task-list')


class PublicTaskApi(TestCase):
    """Tests for unauthorized users"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test login is required for users"""
        res = self.client.get(TASK_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTaskTests(TestCase):
    """Test authorized users"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@gmail.com',
            'password1234',
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieving_tasks(self):
        """Test that tasks are retrieved successfully"""
        Task.objects.create(
            author = self.user,
            title = 'Morning chores',
            task = 'Wake up 7 a.m'
        )
        Task.objects.create(
            author = self.user,
            title = 'Morning rituals',
            task = 'Wake up 9.30 a.m',
        )
        
        tasks = Task.objects.all()
        res = self.client.get(TASK_URL)
        serializer = TaskSerializer(tasks, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_tasks_limited_to_authorized_user(self):
        """Test that only tasks for the auhtenticated user are returned"""
        user2 = get_user_model().objects.create_user(
            'other@gmail.com',
            'testpass098'
        )
        Task.objects.create( author = user2,
            title = 'Morning rituals',
            task = 'Wake up 9.30 a.m')
        task = Task.objects.create(
            author = self.user,
            title = 'Morning chores',
            task = 'Wake up 7 a.m'
        )

        res = self.client.get(TASK_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['title'], task.title)

    

    