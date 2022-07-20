from urllib import request
from contact_queries.models import User_Messages
from django.http import HttpResponseRedirect

def contact(request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        description = request.POST.get('description')
        en = User_Messages(name = name , email = email , Subject = subject , Description = description )
        en.save()

