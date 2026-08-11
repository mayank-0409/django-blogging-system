from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Category

# Create your views here.

def posts_by_category(request, category_id):

    # Fetch the post that belongs to the category with the id category_id
    posts = Blog.objects.filter(status='Published', category=category_id)

    # Method 1 - Use try/except when we want to do some custom action if the category does not exists
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home') # Redirect user to home page

    # Method 2 - Use get_object_or_404 when you want to show 404 error page if the category does not exists
    # category = get_object_or_404(Category, pk=category_id)

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'category.html', context)


def blogs(request, slug):
    single_post = get_object_or_404(Blog, slug=slug, status='Published')
    context = {
        'single_post': single_post
    }
    return render(request, 'blogs.html', context)
