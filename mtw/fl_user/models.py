from django.db import models
from login.models import User
from django.db.models.signals import pre_save
import mutagen

# Create your models here.

class Job_status(models.Model):
    job_id = models.AutoField(primary_key=True)
    Doctor_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='doctor', limit_choices_to={'user_designation' : 'doctor'})

    date_submitted = models.DateTimeField(auto_now_add=True)
    turn_around_time_hr = models.IntegerField()
    audio_name = models.CharField(max_length=100)
    assign_first_level_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='first_level_user', limit_choices_to={'user_designation' : 'first level user'}, null=True)

    assign_second_level_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='second_level_user',limit_choices_to={'user_designation': 'second level user'}, null=True)

    audio_file = models.FileField(blank=True)
    duration = models.CharField(max_length=100,blank=True,default="Audio Not Uploaded")
    Transcription_document = models.FileField(blank=True, null=True)
    feedback = models.TextField(max_length=500, blank=True)
    feedback_given = models.BooleanField(default=False)

    is_asigned = models.BooleanField(default=False)
    transcription_completed = models.BooleanField(default=False)
    QA_passed = models.BooleanField(default=False)

    def __str__(self):
        return self.Doctor_user.email

def duration_finder(sender, instance, raw, using, update_fields, **kwargs):
    file_was_updated = False
    if hasattr(instance.audio_file, 'file'):
        file_was_updated = True

    if update_fields and "audio_file" in update_fields:
        file_was_updated = True

    if file_was_updated:
        # read audio file metadata
        audio_info = mutagen.File(instance.audio_file).info
        # set audio duration in seconds, so we can access it in database
        d=""
        d=d+str(int(audio_info.length)//60)
        d=d+":"
        d=d+str(int(audio_info.length)%60)
        d=d+" Mins"
        instance.duration = d
        #print("audio duration was was updated")

pre_save.connect(duration_finder, sender=Job_status)
