from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from authenticate.forms import RegistrationForm


def landing(request):
    return render(request, 'authenticate/landing.html', {})



def registration_view(request):
    context = {}     
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email,password=raw_password)
            login(request,account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request,'authenticate/register.html',context)


def logout_view(request):
    logout(request)
    return redirect('home')




# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, ('hi '+ str(username) +' ,You have successfully logged in!'))
#             return redirect('landing')
#         else:
#             messages.success(request, ('Error Logging in- Please Try Again....'))
#             return redirect('login')
#     else:
#         return render(request, 'authenticate/login.html', {})


# def logout_user(request):
#     logout(request)
#     messages.success(request,('You have been logged out... | Until next time.'))
#     return redirect('landing')


# def register_user(request):
#     if request.method== "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username= form.cleaned_data['username']
#             password= form.cleaned_data['password1']
#             user = authenticate(username=username, password=password)
#             login(request,user)
#             messages.success(request,('You have Registered.'))
#             return redirect('landing')

#     else:

#         form = UserCreationForm()
#     context ={'form': form}
#     return render(request, 'authenticate/register.html', context)