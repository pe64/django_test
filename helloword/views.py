# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from helloword.models import userinfo


# Create your views here.

def hello(request):
    context = {}
    context['title'] = 'Hello World!'
    context['context'] = "hello word!"
    return render(request, 'index.html', context)
def index(request):
    context = {}
    context['title'] = 'index'
    context['context'] = 'hello word'
    user_list = userinfo.objects.all()
    #return render(request, 'index.html',{'user_list':user_list})
    return render(request, 'login.html', {'user_list': user_list})