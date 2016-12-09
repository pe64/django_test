# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from helloword.models import userinfo
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response,render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.template.context import RequestContext

from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


from django.contrib.auth.decorators import login_required


# Create your views here.

class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


def hello(request):
    context = {}
    context['username'] = 'Hello World!'
    context['password'] = "hello word!"
    return render(request, 'index.html', {'username':request.session['username'],'password':request.session['password']})

def index(request):
    #user_list = userinfo.objects.all()

    if request.method == 'POST':
        uf = UserForm(request.POST)

        if uf.is_valid():
            print(uf.cleaned_data['username'])
            print(uf.cleaned_data['password'])
            request.session['username'] = uf.cleaned_data['username']
            request.session['password'] = uf.cleaned_data['password']
            #return render_to_response('index.html', RequestContext(request, {'username': uf.cleaned_data['username'], 'password': uf.cleaned_data['password']}))
            return HttpResponseRedirect('/helloword/')
            #return render(request, 'index.html',{'user_list':user_list})
    return render(request, 'login.html')