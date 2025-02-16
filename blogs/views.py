from django.shortcuts import render,redirect
from .models import Blog
from . import forms

# Create your views here.
def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/blogs.html', {'blogs': blogs})

def blogDetails(request, pk):
    blog = Blog.objects.get(pk=pk)
    return render(request,  'blogs/blogDetails.html', {'blog' : blog} )


def addBlog(request):
    if request.method == 'POST':
        form = forms.createPost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs')
    else:
        form = forms.createPost()
    return render(request, 'blogs/addBlog.html', {'form': form})
