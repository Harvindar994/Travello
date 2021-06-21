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

        if confirmPassword == password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already used.")
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exits.")
                return redirect('registration')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=frist_name,
                                                last_name=last_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "password is not matching.")
            return redirect('registration')
    else:
        return render(request, 'registration.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'username or password is invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
