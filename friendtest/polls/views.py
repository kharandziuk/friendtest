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

    #def form_invalid(self, form):
    #    return self.render_to_response(self.get_context_data(form=form))

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


class PollShare(DetailView):
    model = models.Poll
    template_name = 'poll/share.html'


class PollParticipate(CreateView):
    model = models.Poll
    template_name = 'poll/create.html'
    fields = ['name', 'answer', 'reference_poll']

    def get_initial(self):
        # Get the initial dictionary from the superclass method
        initial = super(PollParticipate, self).get_initial()
        # Copy the dictionary so we don't accidentally change a mutable dict
        initial = initial.copy()
        initial['reference_poll'] = self.kwargs['reference_poll_pk']
        return initial

    def get_success_url(self):
        return self.object.get_compare_url()


class PollCompare(DetailView):
    model = models.Poll
    template_name = 'poll/compare.html'

    def get_context_data(self, **kwargs):
       context = super(PollCompare, self).get_context_data(**kwargs)
       context['reference_name'] = self.object.reference_poll.name
       context['score'] = self.object.get_comparison_score()
       return context
