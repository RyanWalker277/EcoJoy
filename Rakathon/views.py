from django.shortcuts import render
from testimonials.models import Testimonials
from plants.models import Plants
from blog.models import Blogs
from django.shortcuts import get_object_or_404

def home(request):
    testimonials = Testimonials.objects.all()
    plants = Plants.objects.all()
    blogs = Blogs.objects.all()
    context = {'testimonials' : testimonials , 'plants' : plants , 'blogs' : blogs}
    return render(request , 'index.html' , context)

def about(request):
    testimonials = Testimonials.objects.all()
    context = {'testimonials' : testimonials}
    return render(request , 'about.html' , context)

def shop(request):
    plants = Plants.objects.all()
    context = {'plants' : plants}
    return render(request , 'shop.html' , context)

def blog(request):
    return render(request , 'blog.html')

# def blogpage(request):
#     product = get_object_or_404(Blogs, id)
#     context = {'product': product}
#     return render(request , 'blogpage.html' , context)

def blogpage(request, id):
    blog = Blogs.objects.filter(id=id)
    # print(blog.Title)
    context = {'blog':blog[0]}
    return render(request , 'blogpage.html' , context)