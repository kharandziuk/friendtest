from django.shortcuts import render
from django.views.generic.edit import CreateView
from . import models

class PollCreate(CreateView):
    model = models.Poll
    fields = ['name']
    template_name = 'index.html'

