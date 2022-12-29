from django.urls import path

from main.views import TaskListCreateView, TaskDetailView

# from main.views import TaskListCreateApiView, TaskDetailApiView

# from main.views import tasks_list, task_detail, task_create, task_update, task_delete

urlpatterns = [
    path ('tasks/', TaskListCreateView.as_view()),
    path ('tasks/<int:pk>/', TaskDetailView.as_view()),

    # class urls
    # path('tasks/', TaskListCreateApiView.as_view()),
    # path('tasks/<int:pk>/', TaskDetailApiView.as_view()),
]

# urlpatterns = [
#     # path('tasks/', tasks_list),
#     # path('tasks/<int:pk>/', task_detail),
#     # path('task-create/', task_create),
#     # path('tasks-update/<int:pk>/', task_update),
#     # path('tasks-delete/<int:pk>/', task_delete),
# ]


#http://localhost:8000/api/v1/tasks/    GET: list
#                       ...tasks/<id>/   GET: detail
#
