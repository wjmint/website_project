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

            profile = profile_form.save(commit=False)
            profile.user = user
            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
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
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

        # This is the render and context dictionary to feed
        # back to the registration.html file page.
    return render(request,'basic/registration.html',
                    {'user_form':user_form,
                    'profile_form':profile_form,
                    'registered':registered})