from django.urls import path,include
from .import views
urlpatterns = [
   
    path('add_task/',views.add_task,name='taskpage'),
    path('edit/<int:id>', views.edit_task, name='edit_task'),
    path('delete/<int:id>', views.delete_task, name='delete_task'),
    
   
]
