from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):

    posts = Post.objects.all()

    context = {
        'posts':posts
    }
    return render(request, 'index.html', context=context)

@login_required(login_url='login')
def upload(request):
    if request.method == "POST":
        if 'title' in request.POST:
            name = request.POST["title"]
            content = request.POST["content"]
            q = UploadBlog(author=request.user, title=title, content=content)
            q.save()
            messages.success(request, "Blog has uploaded!")
        else:
            blog_id = list(request.POST.keys())[1]
            del_blog = UploadBlog.objects.filter(user=request.user, id=blog_id)
            del_blog.delete()
            messages.success(request, "Blog removed from Uploaded!")


    blogs = UploadBlog.objects.filter(user=request.user).distinct()
    context = {'blogs': blogs}
    return render(request, 'upload.html', context=context)