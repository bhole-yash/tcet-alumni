from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def landing(request):
    return render(request, 'authenticate/landing.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have successfully logged in!'))
            return redirect('landing')
        else:
            messages.success(request, ('Error Logging in- Please Try Again....'))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})
