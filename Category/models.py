from django.db import models
from Task.models import Task
# Create your models here.
class Category(models.Model):
    CategoryName = models.CharField(max_length=50,)
    task = models.ManyToManyField(Task,related_name='categories')

    def __str__(self) -> str:
        return f'{self.CategoryName}'