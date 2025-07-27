from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import signup_form, email_change_form, avatar_change_form
from django.http import JsonResponse

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

@login_required
def email_change(request):
    if request.method == 'GET':
        form = email_change_form(request.user)
        return render(request, "email_change.html", {'form':form})

    if request.method=='POST':
        form = email_change_form(request.user,request.POST)
        if form.is_valid():
            user = request.user
            u = User.objects.get(username=user)
            u.email = form.cleaned_data['new_email1']
            u.save()
            return redirect("/accounts/profile/")
        else:
            return render(request, "email_change.html", {'form':form})

@login_required
def avatar_change(request):
    if request.method=='POST':
        form = avatar_change_form(request.user, request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('yes')
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': form.errors})
        return JsonResponse({'status': 'wtf'})