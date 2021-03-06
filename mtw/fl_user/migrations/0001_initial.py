# Generated by Django 3.2.5 on 2021-07-18 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_status',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('turn_around_time_hr', models.IntegerField()),
                ('audio_name', models.CharField(max_length=100)),
                ('audio_file', models.FileField(blank=True, upload_to='')),
                ('duration', models.CharField(blank=True, default='Audio Not Uploaded', max_length=100)),
                ('Transcription_document', models.FileField(blank=True, null=True, upload_to='')),
                ('feedback', models.TextField(blank=True, max_length=500)),
                ('feedback_given', models.BooleanField(default=False)),
                ('is_asigned', models.BooleanField(default=False)),
                ('transcription_completed', models.BooleanField(default=False)),
                ('QA_passed', models.BooleanField(default=False)),
                ('expiration_date', models.DateTimeField(default=None)),
                ('Doctor_user', models.ForeignKey(limit_choices_to={'user_designation': 'doctor'}, on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL)),
                ('assign_first_level_user', models.ForeignKey(limit_choices_to={'user_designation': 'first level user'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_level_user', to=settings.AUTH_USER_MODEL)),
                ('assign_second_level_user', models.ForeignKey(limit_choices_to={'user_designation': 'second level user'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_level_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
