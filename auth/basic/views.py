from django.shortcuts import render
from basic import forms

# Create your views here.
def register(request):
    registered = False

    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()

            # Hashing password before saving it
            user.set_password(user.password)
            user.save()