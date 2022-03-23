from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/posts.html", {'post':post})

def post(request, post_id):
    post=get_object_or_404(Post, id=post_id)

    posts = Post.objects.all()

    return render(request, "blog/sample.html", {'post':post})