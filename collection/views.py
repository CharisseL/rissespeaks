from django.shortcuts import render
from collection.models import Story

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {
        'posts': posts,
    })
