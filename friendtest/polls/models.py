from django.db import models
from django.urls import reverse

class Poll(models.Model):
    name = models.CharField(max_length=255)

    def get_share_url(self):
        return reverse('share', args=(self.pk,))

    def get_participate_url(self):
        return reverse('participate', args=(self.pk,))
