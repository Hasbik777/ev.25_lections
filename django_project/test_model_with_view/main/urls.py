from django.urls import path

from .views import StudentAPIView

#http://localhost:8000/api/v1/student/
urlpatterns = [
    path('lists/', StudentAPIView.as_view()),
    path('delete/<int:id>/', StudentAPIView.as_view())
]