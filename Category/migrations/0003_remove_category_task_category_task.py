# Generated by Django 5.0.6 on 2024-06-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0002_remove_category_task_category_task'),
        ('Task', '0004_rename_taskassigndate_task_taskassigndate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='task',
        ),
        migrations.AddField(
            model_name='category',
            name='task',
            field=models.ManyToManyField(related_name='categories', to='Task.task'),
        ),
    ]
