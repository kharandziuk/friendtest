# Generated by Django 2.2.1 on 2019-05-29 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_poll_reference_poll'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='answer',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No'), ('D', 'Don`t know')], default='Y', max_length=1),
            preserve_default=False,
        ),
    ]
