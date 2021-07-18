import io
import os
import re
from datetime import datetime, time, timedelta

import docx
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, FileResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from fl_user.forms import Job_status_form
from fl_user.models import Job_status
from login.models import User
from openpyxl import Workbook
from openpyxl.styles import Font


# Create your views here.
@login_required(login_url='login:auth_login')
def receive_data(request):
    form = Job_status_form()

    if request.is_ajax():
        form = Job_status_form(request.POST or None, request.FILES or None)
        if form.is_valid():
            jb_status = form.save(commit=False)
            jb_status.Doctor_user = request.user
            jb_status.expiration_date = timezone.now() + timedelta(days=150)
            jb_status.audio_name = request.FILES['audio_file']
            jb_status.save()

            return JsonResponse({'message': 'completed'})
    context = {
        'form': form,
    }
    return render(request, 'index.html', {'form': form})


@login_required(login_url='login:auth_login')
def doctorhome(request):
    return render(request, 'doctorhome.html')


@login_required(login_url='login:auth_login')
def fluhome(request):
    return render(request, 'fluhome.html')


@login_required(login_url='login:auth_login')
def sluhome(request):
    return render(request, 'sluhome.html')


@login_required(login_url='login:auth_login')
def view_task_flu(request):
    if request.is_ajax():
        files = request.FILES.dict()
        for i in files.keys():
            jb = Job_status.objects.get(job_id=int(i))
            jb.Transcription_document = files[i]
            jb.transcription_completed = True

            jb.save()
        return HttpResponse(reverse('fl_user:view_task_flu'))

    jobs = Job_status.objects.filter(assign_first_level_user=request.user, transcription_completed=False,
                                     is_asigned=True)
    return render(request, 'view_task_flu.html', {"jobs": jobs})


@login_required(login_url='login:auth_login')
def view_task_doc(request):
    if request.is_ajax():
        files = request.FILES.dict()
        feed_back = request.POST.dict()
        feed_back.pop('csrfmiddlewaretoken')

        for i in files.keys():
            jb = Job_status.objects.get(job_id=int(i))
            os.remove(jb.audio_file.path)
            jb.audio_file = files[i]
            jb.save()

        for i in feed_back.keys():
            if (feed_back[i] != ""):
                jb = Job_status.objects.get(job_id=int(i))
                jb.feedback = feed_back[i]
                jb.feedback_given = True
                jb.save()
        return HttpResponse(reverse('fl_user:view_task_doc'))

    jobs = Job_status.objects.filter(Doctor_user=request.user)
    return render(request, 'view_task_doc.html', {"jobs": jobs})


@login_required(login_url='login:auth_login')
def view_task_slu(request):
    if request.is_ajax():
        files = request.FILES.dict()
        checked = request.POST.dict()
        for i in files.keys():
            jb = Job_status.objects.get(job_id=int(i))
            os.remove(jb.Transcription_document.path)
            jb.Transcription_document = files[i]
            jb.QA_passed = True
            jb.expiration_date = timezone.now() + datetime.timedelta(days=60)
            jb.save()
        checked.pop('csrfmiddlewaretoken')
        for i in checked.keys():
            jb = Job_status.objects.get(job_id=int(i))
            if (checked[i] == 'True'):
                jb.QA_passed = True
                jb.save()

        return HttpResponse(reverse('fl_user:view_task_slu'))

    jobs = Job_status.objects.filter(assign_second_level_user=request.user, transcription_completed=True,
                                     is_asigned=True, QA_passed=False)
    return render(request, 'view_task_slu.html', {"jobs": jobs, "user": "slu"})


# to perform word count on a document
def count_txt(file_name):
    file_name = str(os.path.basename(file_name.name))
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_DIR = os.path.join(BASE_DIR, 'media')
    MEDIA_DIR = os.path.join(MEDIA_DIR, file_name)
    document = docx.Document(MEDIA_DIR)

    newparatextlist = []
    for paratext in document.paragraphs:
        newparatextlist.append(paratext.text)

    return len(re.findall(r'\w+', '\n'.join(newparatextlist))) // 64


@login_required(login_url='login:auth_login')
def generate_report(request):
    wb = Workbook()
    ws1 = wb.active
    ws1.title = "Report"
    ws1.column_dimensions['A'].width = 50
    today = timezone.now().date()
    today_start = datetime.combine(today, time())

    TOTAL_JOBS_RECEIVED_DAILY = ['Total job count today', str(
        Job_status.objects.filter(date_submitted__gte=today_start).count())]
    TOTAL_JOBS_COMPLETED_DAILY = ['Total job completed today is ', str(
        Job_status.objects.filter(date_submitted__gte=today_start, QA_passed=True).count())]

    ws1.append(['Daily report'])
    ws1['A1'].font = Font(bold=True)
    ws1.append(TOTAL_JOBS_RECEIVED_DAILY)
    ws1.append(TOTAL_JOBS_COMPLETED_DAILY)
    ws1.append(['Daily work completion by first level users :'])
    flu = User.objects.filter(user_designation='first level user')
    for i in flu:
        FLU_TASK_COMPLETION = [i.email, str(
            Job_status.objects.filter(date_submitted__gte=today_start, transcription_completed=True,
                                      assign_first_level_user=i).count())]
        ws1.append(FLU_TASK_COMPLETION)

    ws1.append(['Daily work completion by second level users :'])
    slu = User.objects.filter(user_designation='second level user')
    for i in slu:
        SLU_TASK_COMPLETION = [i.email, str(
            Job_status.objects.filter(date_submitted__gte=today_start, QA_passed=True,
                                      assign_second_level_user=i).count())]
        ws1.append(SLU_TASK_COMPLETION)

    total_line_count = 0
    ws1.append(['Total lines processed by first level users :'])
    for i in flu:
        jobs = Job_status.objects.filter(date_submitted__gte=today_start, transcription_completed=True,
                                         assign_first_level_user=i)
        ind_line_count = 0
        for j in jobs:
            ind_line_count += count_txt(j.Transcription_document)
        FLU_TASK_COMPLETION = [i.email, str(
            ind_line_count)]
        ws1.append(FLU_TASK_COMPLETION)
        total_line_count += ind_line_count

    ws1.append(['Total lines processed by second level users :'])
    for i in slu:
        jobs = Job_status.objects.filter(date_submitted__gte=today_start, transcription_completed=True,
                                         assign_second_level_user=i)
        ind_line_count = 0
        for j in jobs:
            ind_line_count += count_txt(j.Transcription_document)
        SLU_TASK_COMPLETION = [i.email, str(
            ind_line_count)]
        ws1.append(SLU_TASK_COMPLETION)

    TOTAL_LINES_PROCESSED = ['Total lines processed today is ', str(total_line_count)]
    ws1.append(TOTAL_LINES_PROCESSED)

    buffer = io.BytesIO()
    wb.save(buffer)
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='WORK_REPORT.xlsx')
