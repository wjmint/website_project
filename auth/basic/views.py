from django import http
from django.shortcuts import render
from basic.forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'basic/index.html')

@login_required
def special(request):
    # remember to also set login url in setting.py
    # Login_URL = '/basic/user_login/'
    return HttpResponse('Succesfully logined')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()

            # Hashing password before saving it
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found profile picture')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
        # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

        # This is the render and context dictionary to feed
        # back to the registration.html file page.
    return render(request,'basic/registration.html',
                    {'user_form':user_form,
                    'profile_form':profile_form,
                    'registered':registered})

def user_login(request):
    if request.method == 'POST':
        # First get the username and password suppiled
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username = username, password = password)

        # If we have a user
        if user:
            # check if the account is active
            if user.is_active:
                # Login granted
                login(request, user)
                # Send the user back to some page
                # In this case, we send them to the homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active
                return HttpResponse('Your account is not active.')
        else:
            print('login try failed')
            return HttpResponse('Invalid login details supplied')
    else:
        return render(request, 'basic/login.html')

def user_info(request):
    return render(request, 'basic/user_info.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))