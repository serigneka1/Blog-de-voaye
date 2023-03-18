from django.shortcuts import render
from blog.models import Post
# Create your views here.

def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE).order_by('-created_at')
    return render(request, 'page/frontpage.html', {'posts':posts})

def about(request):
    return render(request, 'page/about.html')

