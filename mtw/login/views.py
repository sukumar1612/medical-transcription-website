from django.shortcuts import render
from django.http import HttpResponse

from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def login(request):
    return render(request, 'fl_login/login.html')


def register(request):
    return render(request, 'fl_login/registeration.html')