from django.shortcuts import render
from . import forms
from .forms import User

# Create your views here.
def index(request):
    return render(request, 'first/index.html')

def User(request):
    form = forms.User()
    if request.method =='POST':
        form = forms.User(request.POST)

        if form.is_valid():
            print('First Name:', form.cleaned_data['first_name'])
            print('Last Name:', form.cleaned_data['last_name'])
            print('E-mail:', form.cleaned_data['email'])
            print('password:', form.cleaned_data['password'])
            form.save()


    return render(request, 'first/form.html', {'form': form})