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

    def get_share_url(self):
        return reverse('share', args=(self.pk,))

    def get_compare_url(self):
        return reverse('compare', args=(self.pk,))

    def get_participate_url(self):
        return reverse('participate', args=(self.pk,))

    def get_comparison_score(self):
        # example of assertion. If the app doesn't hold this property then we lost data integrity and everything fucked up
        assert self.answers.count()  == self.reference_poll.answers.count()
        score = sum(
            1 for l, r in zip(self.answers.all(), self.reference_poll.answers.all())
            if l.value == r.value
        )
        return int(float(score) / self.answers.count() * 100)


class Question(models.Model):
    value = models.CharField(max_length=255)

    def get_random_questions(self):
        return models.Question.objects.order_by('?')[:settings.QUESTIONS_NUMBER]


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    value = models.CharField(max_length=1, choices=POSSIBLE_ANSWERS)
    poll = models.ForeignKey(Poll, related_name='answers', on_delete=models.CASCADE)
