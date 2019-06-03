from django.core.management.base import BaseCommand, CommandError
from polls.models import Question

class Command(BaseCommand):
    help = 'Adds questions'

    def handle(self, *args, **options):
        questions = [
                'What shows are you into?',
                'What’s your claim to fame?',
                'How often do you play sports?',
                'Are you usually early or late?',
                'What quirks do you have?',
                'How often do you people watch?',
                'What’s your favorite drink?',
                'What do you hope never changes?',
                'What’s your dream car?',
                'Where would you rather be from?',
                'What songs have you completely memorized?',
                'What would you rate 10 / 10?',
                'What job would you be terrible at?',
                'What are you absolutely determined to do?',
                ]
        for q in questions:
            Question.objects.create(value=q)

