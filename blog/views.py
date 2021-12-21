from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Image

def posts(request):
    posts = Post.objects.all()
    return render(request, "index.html", {'posts': posts})


    
def post(request, post_id):
    posts = Post.objects.filter(id=post_id)
    image = Image.objects.filter(post = posts[0])
    return render(request, "post.html", {'posts': posts, 'images': image})