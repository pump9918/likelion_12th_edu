from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.files.storage import default_storage

from .models import Blog

# Create your views here.
def mainpage(request):
    context = {
        'generation': 12,
        'members': ['현아', '영심이', '티준'],
        'info':{'weather': '좋음', 'feeling': '배고픔(?)', 'note': '아기사자 화이팅!'}
    }
    return render(request, 'main/mainpage.html', context)

def secondpage(request):
    blogs = Blog.objects.all()
    return render(request, 'main/secondpage.html', {'blogs': blogs})

def new_blog(request):
    return render(request, 'main/new-blog.html')

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'main/detail.html', {'blog': blog})

def edit(request, id):
    edit_blog = Blog.objects.get(pk=id)
    return render(request, 'main/edit.html', {'blog': edit_blog})

def create(request):
    new_blog = Blog()
    
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()
    new_blog.image = request.FILES.get('image')
    
    new_blog.save()
    
    return redirect('main:detail', new_blog.id)

def update(request, id):
    update_blog = Blog.objects.get(pk=id)
    
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.image = request.FILES.get('image')
    
    update_blog.save()
    
    return redirect('main:detail', update_blog.id)

def delete(request, id):
    delete_blog = Blog.objects.get(pk=id)
    delete_blog.delete()
    default_storage.delete(delete_blog.image.path)
    return redirect('main:secondpage')