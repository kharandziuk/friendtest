from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from . import models

class PollCreate(CreateView):
    model = models.Poll
    fields = ['name', 'answer']
    template_name = 'poll/create.html'

    def get_success_url(self):
        return self.object.get_share_url()


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
