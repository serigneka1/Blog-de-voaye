from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CommentForm
from .models import Post, Category


def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', category_slug=category_slug, slug=slug)
    else:
        form = CommentForm()
    return render(request, 'blog/detail.html', {'post': post, 'form': form})


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category, status=Post.ACTIVE)
    return render(request, 'blog/category.html', {'category': category, 'posts': posts})


def search(request):
    search_query = request.GET.get('q')
    posts = Post.objects.filter(Q(title__icontains=search_query )|Q(intro__icontains=search_query)|Q(body__icontains=search_query), status=Post.ACTIVE) if search_query else []
    return render(request, 'blog/search.html', {'posts': posts, 'search_query': search_query})
