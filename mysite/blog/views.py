from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post

def paginated_view(request, page_number, template_name):
    posts = Post.objects.all()

    items_per_page = int(request.GET.get('items_per_page', 10))

    paginator = Paginator(posts, items_per_page)

    try:
        page_posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_posts = paginator.page(1)
    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)

    return render(request, template_name, {'page_posts': page_posts, 'items_per_page': items_per_page})

def post_list(request):
    return paginated_view(request, 1, 'blog/post_list.html')

def page2(request):
    return paginated_view(request, 2, 'blog/page2.html')

def page3(request):
    return paginated_view(request, 3, 'blog/page3.html')

def page4(request):
    return paginated_view(request, 4, 'blog/page4.html')

def page5(request):
    return paginated_view(request, 5, 'blog/page5.html')