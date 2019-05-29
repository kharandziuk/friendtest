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

class PollParticipate(UpdateView):
    template_name = 'poll/share.html'
