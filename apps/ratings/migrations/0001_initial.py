# Generated by Django 3.2.13 on 2022-06-19 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rating', models.IntegerField(choices=[(1, 'Poor'), (2, 'Fair'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], default=0, help_text='Poor, Fair, Good, Very Good, Excellent ', verbose_name='Rating of agent')),
                ('comment', models.TextField(verbose_name='Comments')),
                ('agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agent_rating', to='profiles.profile', verbose_name='Agent being Rated')),
                ('rater', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User providing rating')),
            ],
            options={
                'unique_together': {('rater', 'agent')},
            },
        ),
    ]
