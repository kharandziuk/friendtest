import ipdb
from django import forms
from django.forms.models import inlineformset_factory
from django.conf import settings

from . import models

class PollForm(forms.ModelForm):
    class Meta:
        model = models.Poll
        fields = '__all__'


class QuestionModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.value

class AnswerInlineForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = '__all__'

    question = QuestionModelChoiceField(
        queryset=models.Question.objects.all()
    )


class AnswerPartipateInlineForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = '__all__'

    question = QuestionModelChoiceField(
        queryset=models.Question.objects.all(),
        disabled=True
    )


_AnswerInlineFormset = inlineformset_factory(models.Poll,
    models.Answer,
    form=AnswerInlineForm,
    extra=settings.QUESTIONS_NUMBER,
    can_delete=False,
    can_order=False
)


_AnswerParticipateInlineFormset = inlineformset_factory(models.Poll,
    models.Answer,
    form=AnswerPartipateInlineForm,
    extra=settings.QUESTIONS_NUMBER,
    can_delete=False,
    can_order=False
)

class AnswerFormMixin(object):
    def clean(self):
        super().clean()
        number_of_answer = sum(1 for form in self.forms if form.cleaned_data)
        if number_of_answer != len(self.forms):
            raise forms.ValidationError('You should answer all the questions')


class AnswerInlineFormset(AnswerFormMixin, _AnswerInlineFormset):
    def clean(self):
        super().clean()
        number_of_uniq_questions = len(set(
            form.cleaned_data['question'] for form in self.forms
        ))
        if number_of_uniq_questions != len(self.forms):
            raise forms.ValidationError('All the quesionts should be unique')


class AnswerPartipateInlineFormset(AnswerFormMixin, _AnswerParticipateInlineFormset):
    pass
