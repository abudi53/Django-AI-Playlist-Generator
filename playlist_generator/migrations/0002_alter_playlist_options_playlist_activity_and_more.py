# Generated by Django 5.1.4 on 2024-12-20 02:21

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist_generator', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='playlist',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='playlist',
            name='activity',
            field=models.CharField(default='Workout', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playlist',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playlist',
            name='genre',
            field=models.CharField(default='Rock', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playlist',
            name='mood',
            field=models.CharField(default='Sad', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playlist',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='playlist',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='song',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
