from email import message
from urllib import request

from django.shortcuts import render
from contact_queries.models import User_Messages
from django.http import HttpResponseRedirect


def contact_index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        description = request.POST.get("message")
        en = User_Messages(
            name=name, email=email, Subject=subject, Description=description
        )
        en.save()
    return render(request, "contact.html")
