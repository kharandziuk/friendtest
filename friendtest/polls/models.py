from django.db import models
from django.urls import reverse

POSSIBLE_ANSWERS = [
        ('Y', 'Yes'),
        ('N', 'No'),
        ('D', 'Don`t know'),
]

class Poll(models.Model):
    name = models.CharField(max_length=255)
    reference_poll = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    answer = models.CharField(max_length=1, choices=POSSIBLE_ANSWERS)

    def get_share_url(self):
        return reverse('share', args=(self.pk,))

    def get_compare_url(self):
        return reverse('compare', args=(self.pk,))

    def get_participate_url(self):
        return reverse('participate', args=(self.pk,))

    def get_comparison_score(self):
        score = int(self.answer == self.reference_poll.answer)
        return int(score / 1. * 100)
