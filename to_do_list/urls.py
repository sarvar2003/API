from rest_framework.routers import DefaultRouter
from django.urls import path, include

from . import views

router = DefaultRouter()
router.register('', views.TaskListViewset)
router.register('', views.TaskDetailViewSet)

app_name = 'to_do_list'

urlpatterns = [
    path('', include(router.urls) )
]
