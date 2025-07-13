from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import signup_form

# Create your views here.

@login_required
def profile(request):
    return render(request, "profile.html")

def signup(request):
    if request.method == 'GET':
        form = signup_form()
        return render(request, 'signup.html', { 'form': form})

    if request.method == 'POST':
        form = signup_form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form': form})