from django import forms
from fl_user.models import Job_status

class Job_status_form(forms.ModelForm):
    class Meta:
        model = Job_status
        fields = ['turn_around_time_hr', 'audio_file']

class Trans_docs(forms.ModelForm):
    class Meta:
        model = Job_status
        fields = ['Transcription_document']
