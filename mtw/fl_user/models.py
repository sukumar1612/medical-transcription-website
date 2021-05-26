from django.db import models
from login.models import User

class Job_status(models.Model):
    doctor_name = models.CharField(max_length=100)
    date_submitted = models.DateTimeField(auto_now_add=True)
    turn_around_time_hr = models.IntegerField()
    audio_name = models.CharField(max_length=100)
    assign_first_level_user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_designation' : 'first level user'})
    is_asigned = models.BooleanField(default=False)
    transcription_completed = models.BooleanField(default=False)
    QA_passed = models.BooleanField(default=False)

    def __str__(self):
        return self.audio_name
# Create your models here.


