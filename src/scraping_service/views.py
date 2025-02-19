from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    template_name = 'home.html'
    context = {
        'title': 'Home',
        'content': 'Hello world!!!'
    }
    return render(request, template_name=template_name, context=context)




