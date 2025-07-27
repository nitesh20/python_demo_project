from django.urls import path
from task import views

urlpatterns = [
    path('task/list/', views.task_list_view, name='task_list'),
    path('task/', views.add_task_view, name='add_task'),
    path('task/<int:id>/', views.update_task_view, name="update_task"),
    path('task/<int:id>/', views.delete_task_view, name='delete_task'),
]
