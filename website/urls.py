from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('members.html', views.members, name="members"),
    path('authenticate/landing.html', views.landing, name="landing"),
    path('', views.notification_system, 'notification')
]
