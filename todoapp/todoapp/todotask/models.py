
import datetime

from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    task_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    deadline = models.DateTimeField(default=timezone.now()+datetime.timedelta(weeks=1))
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.task_text

    def is_overdue(self):
        return self.deadline <= timezone.now()

    def is_finised(self):
        return self.finished
