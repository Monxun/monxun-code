from django.shortcuts import render
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

# Create your views here.
####################################################################
# HOME
def HomeView(request):
    return render(request, 'home/index.html')


####################################################################
# VBT
def VbtView(request):
    return render(request, 'vbt/vbt.html')

 
####################################################################
# BIZ
def BizView(request):

    with open('home/pages/biz/graphs/monthly.html', 'r') as f:
        monthly = f.read()

    with open('home/pages/biz/graphs/seasonal.html', 'r') as f:
        seasonal = f.read()

    with open('home/pages/biz/graphs/detrender.html', 'r') as f:
        detrender = f.read()

    with open('home/pages/biz/graphs/deseason.html', 'r') as f:
        deseason = f.read()

    with open('home/pages/biz/graphs/forecast.html', 'r') as f:
        forecast = f.read()

    context = {
        'seasonal': seasonal,
    }
    return render(request, 'biz/biz.html', context)


####################################################################
# MUS
def MusView(request):
    return render(request, 'mus/mus.html')