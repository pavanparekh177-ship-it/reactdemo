from django.urls import path
from . import views

urlpatterns = [
    path('', views.getStudents),
    path('add/', views.addStudent),
    path('update/<int:id>/', views.updateStudent),
    path('delete/<int:id>/', views.deleteStudent),
]
