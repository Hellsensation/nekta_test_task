from django.db import models


class Request(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


