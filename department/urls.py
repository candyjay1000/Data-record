from django.urls import path
from .views import *
urlpatterns = [
    path('section', indexpage, name='indexpage'),
    path('add-section', add_department, name='add_section'),
    path('delete/<int:id>/', delete_department, name='delete_section'),
    path('update/<int:id>/', update_department, name='update_section'),
]

