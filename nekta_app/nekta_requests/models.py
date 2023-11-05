from django.contrib.auth.models import User
from django.db import models


class Request(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class RequestMessage(models.Model):
    text = models.TextField(null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    request = models.ForeignKey(Request, on_delete=models.PROTECT)

    def __str__(self):
        return 'Request message'
