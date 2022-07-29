from ast import mod
from django.db import models
import uuid




class Task(models.Model):

    task_id = models.CharField(primary_key=True, default=uuid.uuid1, max_length=100) 
    task_ref_number = models.IntegerField(null = True)
    instructions = models.TextField(blank=True) 
    # file = models.FileField(blank=False, null=False)

    def __str__(self):
        return f'{self.task_id} Task'

class TaskMedia(models.Model):
    task = models.ForeignKey(Task,on_delete=models.CASCADE, null=True, related_name = 'task_media', related_query_name = 'task_media')
    file = models.FileField(null=True)

    def __str__(self):
        return f'{self.task} TaskMedia'
 
