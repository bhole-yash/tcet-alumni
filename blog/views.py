from django.shortcuts import render

from blog.models import BlogPost
# Create your views here.

def create_blog_view(request):
    return render(request,"blog/create_blog.html",{})