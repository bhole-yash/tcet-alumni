from django.shortcuts import render, redirect
from django.core.mail import send_mail


# Create your views here.

def home(request):
    return render(request, 'website/home.html', {})


def home1(request):
    return render(request, 'website/home1.html', {})


def landing(request):
    return redirect('landing')


def about(request):
    return render(request, 'website/about.html', {})


def members(request):
    return render(request, 'website/members.html', {})


def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['comments']

        # send an email
        send_mail(

            'Thanks for Feedback' + first_name,  # Subject

            message,  # message

            email,  # from email

            ["yash.tcet@gmail.com"]
        )

        comments = request.POST['comments']
        return render(request, 'website/contact.html',
                      {"note": "Thanks We received your email and will respond shortly...", "first_name": first_name,
                       "last_name": last_name})
    else:
        return render(request, 'website/contact.html', {})
