from django.urls import path
from .views import *

urlpatterns = [
    path('', welcome, name= 'You are welcome'),
    path('students',students_indexpage, name='students_indexpage'),
    path('add-student', add_student, name='add_student'),
     path('deleted/<int:id>/', delete_student, name='delete_student'),
    path('updated/<int:id>/', update_student, name='update_student'),
]
