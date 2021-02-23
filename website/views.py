from django.shortcuts import render, redirect
from django.core.mail import send_mail
from operator import attrgetter
from django.core.paginator import EmptyPage,PageNotAnInteger, Paginator
from blog.views import get_blog_queryset
from authenticate.models import Account
from blog.models import BlogPost

BLOG_POSTS_PER_PAGE=1
# Create your views here.

def home(request):
    return render(request, 'website/home.html', {})




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


def home_screen_view(request):
	
	context = {}

	query = ""
	if request.GET:
		query = request.GET.get('q','')
		context['query'] = str(query)
	blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)
	context['blog_posts'] = blog_posts

    # Pagination
	page = request.GET.get('page', 1)
	blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)
	try:
		blog_posts = blog_posts_paginator.page(page)
	except PageNotAnInteger:
		blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
	except EmptyPage:
		blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

	context['blog_posts'] = blog_posts

	return render(request, "website/home1.html", context)
