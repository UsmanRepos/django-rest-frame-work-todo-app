import uuid
from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid1)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

class Time(models.Model):
    # todo = models.ForeignKey(Todo, on_delete=models.CASCADE, blank=True, null=True, related_name='todo')
    time_id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class Todo(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="user")
    time = models.ForeignKey(Time, on_delete=models.CASCADE, blank=True, null=True, related_name='time')
    todo_title = models.CharField(max_length=100)
    todo_description = models.TextField()
    is_done = models.BooleanField(default=False)

    
