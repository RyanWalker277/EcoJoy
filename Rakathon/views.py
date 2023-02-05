import base64
import json
from django.shortcuts import render
from testimonials.models import Testimonials
from plants.models import Plants
from blog.models import *
from django.shortcuts import get_object_or_404
import requests


def home(request):
    testimonials = Testimonials.objects.all()
    plants = Plants.objects.all()
    blogs = Blogs.objects.all()
    context = {"testimonials": testimonials, "plants": plants, "blogs": blogs}
    return render(request, "index.html", context)


def about(request):
    testimonials = Testimonials.objects.all()
    context = {"testimonials": testimonials}
    return render(request, "about.html", context)


def shop(request):
    plants = Plants.objects.all()
    context = {"plants": plants}
    return render(request, "shop.html", context)


def plants(request, id):
    plant = Plants.objects.filter(id=id)
    plants_all = Plants.objects.all()
    context = {"plant": plant[0], "plants_all": plants_all}
    return render(request, "product.html", context)


def portfolio(request):
    return render(request, "portfolio.html")


def identifier(request):
    return render(request, "identifier.html")


def identified(request):
    if request.method == "POST" and request.FILES["img_logo"]:
        img_logo = request.FILES["img_logo"]
        images = [base64.b64encode(img_logo.read()).decode("ascii")]

        json = {
            "images": images,
            "plant_details": [
                "common_names",
                "edible_parts",
                "propagation_methods",
                "synonyms",
                "taxonomy",
            ],
        }
        headers = {
            "Content-Type": "application/json",
            "Api-Key": "g9O2aT7oz4HeADWCIXpclLo4BtAvTyyY1u8EcOmYQJEsFnNQtX",
        }
        try:
            r = requests.post(
                "https://api.plant.id/v2/identify", json=json, headers=headers
            )
            r = r.json()
            r = r["suggestions"][0]
            try:
                r["plant_details"]["synonyms"] = r["plant_details"]["synonyms"][:7]
            except:
                pass
        except:
            return render(request, "identifier.html")

        return render(request, "identified.html", {"plant_info": r})

    return render(request, "identifier.html")
