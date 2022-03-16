from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from pypro.base.forms import SignUpForm


def home(request):
    return render(request, 'base/home.html')


def registrar(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password2')
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
