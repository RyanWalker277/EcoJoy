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
    blogs = Blogs.objects.all()
    context = {'blogs' : blogs}
    return render(request , 'blog.html' , context)

def blogpage(request, id):
    blog = Blogs.objects.filter(id=id)
    context = {'blog':blog[0]}
    return render(request , 'blogpage.html' , context)

def plants(request, id):
    plant = Plants.objects.filter(id=id)
    plants_all = Plants.objects.all()
    context = {'plant':plant[0] , 'plants_all':plants_all }
    return render(request , 'product.html' , context)

def portfolio(request):
    return render(request , 'portfolio.html')

def identifier(request):
    return render(request , 'identifier.html')

def identified(request):
    return render(request , 'identified.html')