from django.db import models
# from Category.models import Category
class Task(models.Model):
    taskTitle = models.CharField(max_length=200)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    taskAssignDate = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    # category = models.ManyToManyField(Category)
    def __str__(self):
        return self.taskTitle