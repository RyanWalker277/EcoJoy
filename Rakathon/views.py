from django.shortcuts import render
from testimonials.models import Testimonials
from plants.models import Plants
from blog.models import Blogs

def home(request):
    testimonials = Testimonials.objects.all()
    plants = Plants.objects.all()
    blogs = Plants.objects.all()
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