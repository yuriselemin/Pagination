from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')

    page_size = request.GET.get('page_size', 10)
    paginator = Paginator(posts, page_size)

    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'page_obj': page_obj,
        'page_sizes': [5, 10, 20],  # Возможные варианты количества постов на странице
    }
    return render(request, 'templates/post_list.html', context)