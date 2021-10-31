from django.urls import path
from .views import TaskList, TaskAdd, TaskUpdate, TaskDelete


urlpatterns = [
    path('', TaskList.as_view(), name='list'),
    path('add/', TaskAdd.as_view(), name='add'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='delete'),
]
