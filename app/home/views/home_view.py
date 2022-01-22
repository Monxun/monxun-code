from django.shortcuts import render
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .helpers import (
    CSVToDataFrame,
    MakeDataFrameJson, 
    MakeModelCSV, 
    ImportCSV, 
    TableExportCSV,
    )


# HOME
def HomeView(request):
    return render(request, 'home/index.html')


def RegisterPage(request):
    context = {}
    return render(request, 'accounts/register.html')


def LoginPage(request):
    context = {}
    return render(request, 'accounts/login.html')