import factory

from . import models

class PollFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Poll

    def __init__(self, *args, **kwargs):
        answer = kwargs.pop['answer']
        super().__init__(*args, **kwargs)
        if answer:
            AnswerFactory(value=answer, poll=self)


class AnswerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Answer

