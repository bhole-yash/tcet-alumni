from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

from authenticate.views import (
    registration_view,
    logout_view,
    login_view,
    account_view,
    must_authenticate_view,

)
from website.views import (
    contact, about, members, home, home_screen_view, notification_system
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('website.urls')),
    # path('', include('authenticate.urls')),
    path('notifications/',notification_system, name='notification'),
    path('logout/', logout_view, name='logout'),
    path('must_authenticate', must_authenticate_view, name="must_authenticate"),
    path('register/', registration_view, name='register'),
    path('home1/', home_screen_view, name='home1'),
    path('blog', include('blog.urls', 'blog')),
    path('', home, name="home"),

    path('contact.html', contact, name="contact"),
    path('about.html', about, name="about"),
    path('members.html', members, name="members"),
    path('login/', login_view, name="login"),
    path('account/', account_view, name="account"),
    # path('account/',include('django.contrib.auth.urls')),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration'
                                                                                          '/password_change_done.html'),
         name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration'
                                                                                            '/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration'
                                                                                   '/password_reset_complete.html'),
         name='password_reset_complete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
