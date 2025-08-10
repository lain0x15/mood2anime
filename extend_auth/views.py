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
        return render(request, 'signup.html', {'form': signup_form()})

    if request.method == 'POST':
        form = signup_form(request.POST)
        if not form.is_valid():
            return render(request, 'signup.html', {'form': form})
        user = form.save(commit=False)
        user.save()
        login(request, user)
        return redirect('/')

@login_required
def email_change(request):
    if request.method == 'GET':
        return render(request, "email_change.html", {'form':email_change_form(request.user)})

    if request.method=='POST':
        form = email_change_form(request.user,request.POST)
        if not form.is_valid():
            return render(request, "email_change.html", {'form':form})
        user = request.user
        u = User.objects.get(username=user)
        u.email = form.cleaned_data['new_email1']
        u.save()
        return redirect("/accounts/profile/")


@login_required
def avatar_change(request):
    if request.method=='POST':
        form = avatar_change_form(request.user, request.POST, request.FILES)
        if not form.is_valid():
            return JsonResponse({'status': form.errors})
        form.save()
        return JsonResponse({'status': 'ok'})