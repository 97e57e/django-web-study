from django.shortcuts import render,redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .models import Portfolio

# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request,'home.html',{'blogs' : blogs})

def new(request):
    return render(request,'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()

    return redirect('/')


def portfolio(request):
    portfolios=Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios' : portfolios})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)

    return render(request,'detail.html',{'blog' : blog_detail})

def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('/')

def edit(request, blog_id):
    blog_edit =Blog.objects.get(id=blog_id)
    return render(request, 'edit.html',{'blog' : blog_edit})

def update(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()

    return redirect('/blog/'+ str(blog_id))