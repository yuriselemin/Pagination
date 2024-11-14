from django.core.paginator import Paginator
from django.shortcuts import render
from .forms import ItemsPerPageForm
from .models import Post

def post_list(request):
    items_per_page = request.GET.get('items_per_page', '3')
    form = ItemsPerPageForm(request.GET or None)

    if form.is_valid():
        items_per_page = form.cleaned_data['items_per_page']

    page_posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(page_posts, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'form': form,
        'page_posts': page_obj,
        'items_per_page': int(items_per_page),
    }

    return render(request, 'blog/post_list.html', context)



















    # def paginated_view(request, page_number, template_name):
#     posts = Post.objects.all()
#
#     items_per_page = int(request.GET.get('items_per_page', 5))
#
#     paginator = Paginator(posts, items_per_page)
#
#     try:
#         page_posts = paginator.get_page(page_number)
#     except PageNotAnInteger:
#         page_posts = paginator.page(page_number)
#     except EmptyPage:
#         page_posts = paginator.page(paginator.num_pages)
#
#     return render(request, template_name, {'page_posts': page_posts, 'items_per_page': items_per_page})
#
# def post_list(request):
#     return paginated_view(request, 1, 'blog/post_list.html')
#
# def page2(request):
#     return paginated_view(request, 2, 'blog/page2.html')
#
# def page3(request):
#     return paginated_view(request, 3, 'blog/page3.html')
#
# def page4(request):
#     return paginated_view(request, 4, 'blog/page4.html')
#
# def page5(request):
#     return paginated_view(request, 5, 'blog/page5.html')