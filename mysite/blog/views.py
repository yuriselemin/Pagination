from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post


def post_list(request):
    # Get all posts
    posts = Post.objects.all()

    # Get the selected number of items per page from the request
    items_per_page = int(request.GET.get('items_per_page', 10))

    # Create a paginator with the selected number of items per page
    paginator = Paginator(posts, items_per_page)

    # Get the page number from the request
    page_number = request.GET.get('page')
    try:
        page_posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_posts = paginator.page(1)
    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_list.html',
                                {'page_posts': page_posts, 'items_per_page': items_per_page})

def page2(request):
    # Get all posts
    posts = Post.objects.all()

    # Get the selected number of items per page from the request
    items_per_page = int(request.GET.get('items_per_page', 10))

    # Create a paginator with the selected number of items per page
    paginator = Paginator(posts, items_per_page)

    # Get the page number from the request
    page_number = request.GET.get('page')
    try:
        page_posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_posts = paginator.page(1)
    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/page2.html',
                                {'page_posts': page_posts, 'items_per_page': items_per_page})

def page3(request):
    # Get all posts
    posts = Post.objects.all()

    # Get the selected number of items per page from the request
    items_per_page = int(request.GET.get('items_per_page', 10))

    # Create a paginator with the selected number of items per page
    paginator = Paginator(posts, items_per_page)

    # Get the page number from the request
    page_number = request.GET.get('page')
    try:
        page_posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_posts = paginator.page(1)
    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/page3.html',
                                {'page_posts': page_posts, 'items_per_page': items_per_page})

def page4(request):
    # Get all posts
    posts = Post.objects.all()

    # Get the selected number of items per page from the request
    items_per_page = int(request.GET.get('items_per_page', 10))

    # Create a paginator with the selected number of items per page
    paginator = Paginator(posts, items_per_page)

    # Get the page number from the request
    page_number = request.GET.get('page')
    try:
        page_posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_posts = paginator.page(1)
    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/page4.html',
                                {'page_posts': page_posts, 'items_per_page': items_per_page})

def page5(request):
    # Get all posts
    posts = Post.objects.all()

    # Get the selected number of items per page from the request
    items_per_page = int(request.GET.get('items_per_page', 10))

    # Create a paginator with the selected number of items per page
    paginator = Paginator(posts, items_per_page)

    # Get the page number from the request
    page_number = request.GET.get('page')
    try:
        page_posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_posts = paginator.page(1)
    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/page5.html',
                                {'page_posts': page_posts, 'items_per_page': items_per_page})
