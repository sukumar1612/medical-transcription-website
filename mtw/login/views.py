from django.shortcuts import render
from django.http import HttpResponse

from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

from login.forms import UserForm, UserProfileInfoForm
from login.models import CustomUser
from django.http import JsonResponse

# Create your views here.


def auth_login(request):

    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        username = ''
        try:
            username=CustomUser.objects.get(email=email).username
        except:
            print("error")
        user=authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                print("logged in ")

    return render(request, 'fl_login/login.html')


def registerdoc(request):

    registered = 'reg'

    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        userdata=request.POST.dict()
        userdata['user_designation']='doctor'

        profile_form = UserProfileInfoForm(userdata)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.customuser = user

            profile.save()
            registered = 'Registered successfully'
        else:
            print("error invalid form")
            registered = 'Username already exists'

    return render(request, 'fl_login/registeration.html',{'status':registered})


def registerflu(request):

    registered = 'reg'

    if request.method == "POST":
        user_form = UserForm(data=request.POST)


        userdata=request.POST.dict()
        userdata['user_designation']='first level user'

        profile_form = UserProfileInfoForm(userdata)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.customuser=user

            profile.save()
            registered = 'Registered successfully'

        else:
            print("error invalid form")
            registered = 'User already exists'

    return render(request, 'fl_login/registeration.html',{'status':registered})


def registerslu(request):

    registered = 'reg'

    if request.method == "POST":
        user_form = UserForm(data=request.POST)


        userdata=request.POST.dict()
        userdata['user_designation']='second level user'

        profile_form = UserProfileInfoForm(userdata)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.customuser=user

            profile.save()
            registered = 'Registered successfully'

        else:
            print("error invalid form")
            registered = 'User already exists'

    return render(request, 'fl_login/registeration.html',{'status':registered})