from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from . import models, forms

class PollCreate(CreateView):
    form_class = forms.PollForm
    # fields = ['name', 'answer']
    template_name = 'poll/create.html'

    def form_valid(self, form):
        ctx = self.get_context_data()
        inlines = ctx['inlines']
        if inlines.is_valid() and form.is_valid():
            self.object = form.save()
            inlines.instance = self.object
            inlines.save()
            return redirect(self.get_success_url())
        else:
            return super.form_invalid(form)

    def get_success_url(self):
        return self.object.get_share_url()


    def get_context_data(self, **kwargs):
        ctx = super(PollCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            ctx['form'] = forms.PollForm(self.request.POST)
            ctx['inlines'] = forms.AnswerInlineFormset(self.request.POST)
        else:
            ctx['form'] = forms.PollForm()
            ctx['inlines'] = forms.AnswerInlineFormset()
        return ctx


class PollParticipate(PollCreate):

    def get_success_url(self):
        return self.object.get_compare_url()

    def form_valid(self, form):
        redirection = super().form_valid(form)
        if self.object.pk:
            self.object.reference_poll_id = self.kwargs['reference_poll_pk']
            self.object.save()
        return redirection


class PollShare(DetailView):
    model = models.Poll
    template_name = 'poll/share.html'

class PollCompare(DetailView):
    model = models.Poll
    template_name = 'poll/compare.html'

    def get_context_data(self, **kwargs):
       context = super(PollCompare, self).get_context_data(**kwargs)
       context['reference_name'] = self.object.reference_poll.name
       context['score'] = self.object.get_comparison_score()
       return context
