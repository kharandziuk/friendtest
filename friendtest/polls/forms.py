from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django.conf import settings

from . import models

class PollForm(ModelForm):
    class Meta:
        model = models.Poll
        fields = '__all__'


class AnswerInlineForm(ModelForm):
    class Meta:
        model = models.Answer
        fields = '__all__'


AnswerInlineFormset = inlineformset_factory(models.Poll,
    models.Answer,
    form=AnswerInlineForm,
    extra=settings.QUESTIONS_NUMBER,
    can_delete=False,
    can_order=False
)
