

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from .forms import CustomUserCreationForm


# Create your views here.
def loginView(response):
    return HttpResponse("Login page from dummy view")
def registerView(request):
    if request.method == 'POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            login(request,user)
            # return redirect
    else:
        form=CustomUserCreationForm()   
    return render(request,'user/register.html',{})
    # return HttpResponse("Register Page From Dummy View")
