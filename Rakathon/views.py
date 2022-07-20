from django.shortcuts import render
from testimonials.models import Testimonials
from plants.models import Plants

def home(request):
    testimonials = Testimonials.objects.all()
    context = {'testimonials' : testimonials}
    return render(request , 'index.html' , context)

def about(request):
    testimonials = Testimonials.objects.all()
    context = {'testimonials' : testimonials}
    return render(request , 'about.html' , context)

def shop(request):
    plants = Plants.objects.all()
    context = {'plants' : plants}
    return render(request , 'shop.html' , context)