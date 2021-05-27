from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from fl_user.forms import Job_status_form
from django.http import JsonResponse
from login.models import User

# Create your views here.

@login_required(login_url='/auth/login')
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
            jb_status.audio_name = request.FILES['audio_file']
            jb_status.save()

            return JsonResponse({'message': 'completed'})
    context = {
        'form': form,
    }
    return render(request, 'index.html', {'form' : form})