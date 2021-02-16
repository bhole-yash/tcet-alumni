from django.contrib import admin
from django.urls import path, include

from authenticate.views import (
    registration_view,
    logout_view,
    login_view,
    account_view
)
from website.views import (
    contact, about, members, home
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('website.urls')),
    # path('', include('authenticate.urls')),
    path('logout/', logout_view, name='logout'),
    path('register/', registration_view, name='register'),
    path('', home, name="home"),
    path('contact.html', contact, name="contact"),
    path('about.html', about, name="about"),
    path('members.html', members, name="members"),
    path('login/', login_view, name="login"),
    path('account/', account_view, name="account"),

]
