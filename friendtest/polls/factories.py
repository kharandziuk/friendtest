import factory

from . import models

class PollFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Poll


class AnswerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Answer


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Question

    value = factory.Sequence(lambda n: "What are you # %s" % n)
