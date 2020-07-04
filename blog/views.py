from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.


def all_blogs(request):
    # el [:[number]] sirve para limitar los que se va a mostrar
    # blogs = Blog.objects.order_by('date')[:3]
    blogs = Blog.objects.order_by('date')
    return render (request, 'blogs/all_blogs.html', { 'blogs': blogs })

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/detail.html',{'blog': blog})