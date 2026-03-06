from django.db import models
from users.models import User

class ActivityLog(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    action = models.CharField(max_length=255)

    timestamp = models.DateTimeField(auto_now_add=True)