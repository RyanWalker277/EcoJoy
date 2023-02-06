from django.shortcuts import render


def google(request):
    return render(request, "Login.html")
