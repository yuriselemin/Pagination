from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')

    paginator = Paginator(posts, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog/post_list.html', context)