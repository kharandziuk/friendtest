import ipdb
from django import forms
from django.forms.models import inlineformset_factory
from django.conf import settings

from . import models

class PollForm(forms.ModelForm):
    class Meta:
        model = models.Poll
        fields = '__all__'


class AnswerInlineForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = '__all__'


_AnswerInlineFormset = inlineformset_factory(models.Poll,
    models.Answer,
    form=AnswerInlineForm,
    extra=settings.QUESTIONS_NUMBER,
    can_delete=False,
    can_order=False
)

class AnswerInlineFormset(_AnswerInlineFormset):
    def clean(self):
        super().clean()
        number_of_answer = sum(1 for form in self.forms if form.cleaned_data)
        if number_of_answer != len(self.forms):
            raise forms.ValidationError('You should answer all the questions')

