from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.


def registration(request):
    if request.method == 'POST':
        frist_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']

        user = User.objects.create_user(username=username, password=password, email=email, first_name=frist_name, last_name=last_name)
        user.save()
        print("User Created")
        return redirect('/')
    else:
        return render(request, 'registration.html')