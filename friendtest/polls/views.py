from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from . import models

class PollCreate(CreateView):
    model = models.Poll
    fields = ['name']
    template_name = 'index.html'

    def get_success_url(self):
        return self.object.get_share_url()


class PollShare(DetailView):
    model = models.Poll
    template_name = 'poll/share.html'

class PollParticipate(CreateView):
    model = models.Poll
    template_name = 'index.html'
    fields = ['name', 'reference_poll']

    def get_initial(self):
        # Get the initial dictionary from the superclass method
        initial = super(YourView, self).get_initial()
        # Copy the dictionary so we don't accidentally change a mutable dict
        initial = initial.copy()
        print(self.kwargs['pk'])
        # etc...
        return initial

    def get_success_url(self):
        return self.object.get_merge_url()
