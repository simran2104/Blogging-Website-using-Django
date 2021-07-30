from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    if request.method == "POST":
        if 'title' in request.POST:
            title = request.POST["title"]
            content = request.POST["content"]
            q = Post(author=request.user, title=title, content=content)
            q.save()
            messages.success(request, "Blog has uploaded!")
        elif 'like' in request.POST:
            blog_id = list(request.POST.keys())[1]
            blog = Post.objects.filter(id=blog_id)
            blog.like += 1
            blog.save()
            messages.success(request, "Blog has uploaded!")
        else:
            blog_id = list(request.POST.keys())[1]
            del_blog = Post.objects.filter(id=blog_id)
            del_blog.delete()
            messages.success(request, "Blog removed from Uploaded!")

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
            q = Post(author=request.user, title=title, content=content)
            q.save()
            messages.success(request, "Blog has uploaded!")
        else:
            blog_id = list(request.POST.keys())[1]
            del_blog = Post.objects.filter(user=request.user, id=blog_id)
            del_blog.delete()
            messages.success(request, "Blog removed from Uploaded!")


    blogs = Post.objects.all()
    context = {'blogs': blogs}
    return render(request, 'index.html', context=context)