# Generated by Django 3.0.3 on 2021-06-13 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fl_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_status',
            name='Transcription_document',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]