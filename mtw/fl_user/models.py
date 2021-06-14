from django.db import models
from login.models import User

# Create your models here.

class Job_status(models.Model):
    job_id = models.AutoField(primary_key=True)
    Doctor_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='doctor', limit_choices_to={'user_designation' : 'doctor'})

    date_submitted = models.DateTimeField(auto_now_add=True)
    turn_around_time_hr = models.IntegerField()
    audio_name = models.CharField(max_length=100)
    assign_first_level_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='first_level_user', limit_choices_to={'user_designation' : 'first level user'})

    assign_second_level_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='second_level_user',limit_choices_to={'user_designation': 'second level user'})

    audio_file = models.FileField(blank=True)
    Transcription_document = models.FileField(blank=True, null=True)

    is_asigned = models.BooleanField(default=False)
    transcription_completed = models.BooleanField(default=False)
    QA_passed = models.BooleanField(default=False)

    def __str__(self):
        return self.audio_name




