# Generated by Django 2.2.1 on 2019-05-31 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_poll_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='answer',
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Y', 'Yes'), ('N', 'No'), ('D', 'Don`t know')], max_length=1)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='polls.Poll')),
            ],
        ),
    ]