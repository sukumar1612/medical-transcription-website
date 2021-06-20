from django.shortcuts import render
from django.http import HttpResponse

from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

from django.shortcuts import redirect

from login.forms import UserForm
from login.models import User
from django.http import JsonResponse

import fl_user.views
# Create your views here.

def Logout(request):
	if not request.user.is_active:
		return redirect('login:auth_login')
	logout(request)
	return redirect('login:auth_login')


def auth_login(request):
    error=""
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        user=authenticate(email=email, password=password)

        if user:
            if user.is_active:
                login(request, user)
                print("logged in ", user.user_designation)
                if user.user_designation == 'doctor':
                    return redirect('fl_user:doctorhome')
                elif user.user_designation == 'first level user':
                    return redirect('fl_user:fluhome')
                elif user.user_designation == 'second level user':
                    return redirect('fl_user:sluhome')
                elif user.user_designation == 'staff':
                	return redirect('admin/')
        elif user is None:
           error="yes"

    return render(request, 'fl_login/login.html', {"error":error})
