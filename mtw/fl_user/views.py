from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from fl_user.forms import Job_status_form, Trans_docs
from django.http import JsonResponse
from login.models import User
from .models import Job_status

# Create your views here.

@login_required(login_url='')
def receive_data(request):
    form = Job_status_form()

    if request.is_ajax():
        form = Job_status_form(request.POST or None, request.FILES or None)
        print(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            jb_status = form.save(commit = False)
            jb_status.Doctor_user = request.user
            print(request.user.fullname)
            jb_status.assign_first_level_user = User.objects.get(email= 'sk12@gmail.com')
            jb_status.assign_second_level_user = User.objects.get(email='sk12@gmail.com')
            jb_status.audio_name = request.FILES['audio_file']
            jb_status.save()

            return JsonResponse({'message': 'completed'})
    context = {
        'form': form,
    }
    return render(request, 'index.html', {'form' : form})

def home(request):
    return render(request, 'doctorhome.html')

@login_required(login_url='')
def view_task(request):
    if request.is_ajax():
        files = request.FILES.dict()
        for i in files.keys():
            jb = Job_status.objects.get(job_id = int(i))
            print(jb)
            jb.Transcription_document = files[i]
            jb.transcription_completed = True
            jb.save()
        return HttpResponse(reverse('fl_user:view_task'))

    jobs=Job_status.objects.filter(assign_first_level_user=request.user,transcription_completed=False)
    return render(request,'view_task.html',{"jobs":jobs})

@login_required(login_url='')
def view_task_doc(request):
    jobs=Job_status.objects.filter(Doctor_user=request.user)
    return render(request,'view_task_doc.html',{"jobs":jobs})