from django.db import models

class Poll(models.Model):
    name = models.CharField(max_length=255)
