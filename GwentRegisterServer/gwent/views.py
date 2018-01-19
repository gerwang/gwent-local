# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
# Create your views here.
from django.shortcuts import render
from django.urls import reverse

from .models import Player


def index(request):
    return render(request=request, template_name='gwent/index.html')


def register(request):
    return render(request=request, template_name='gwent/register.html')


def ranklist(request):
    return render(request=request, template_name='gwent/ranklist.html', context={
        'userlist': Player.objects.order_by('-rating')})


def handle(request):
    username = request.POST['username']
    password = request.POST['password']
    if Player.objects.filter(username=username).count() > 0:
        # same user name already exists
        return render(request=request, template_name='gwent/register.html', context={
            'error_message': 'Same user name already exists'
        })
    else:
        Player.objects.create(username=username, password=password)
        return HttpResponseRedirect(reverse('gwent:ranklist'))
