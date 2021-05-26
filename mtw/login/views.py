from django.shortcuts import render
from django.http import HttpResponse

from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

from login.forms import UserForm
from django.http import JsonResponse

# Create your views here.


def auth_login(request):

    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        user=authenticate(email=email, password=password)
        print(user)
        if user:
            if user.is_active:
                login(request, user)

                print("logged in ", user.user_designation)

    return render(request, 'fl_login/login.html')
