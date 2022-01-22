from django.shortcuts import render
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from home.forms import SongSearchForm
from home.models.mus_models import Song, Artist
import json

import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import urllib.request

from .helpers import (

    # GENERAL METHODS
    CSVToDataFrame,
    MakeDataFrameJson, 
    MakeModelCSV, 
    ImportCSV, 
    TableExportCSV,

    # MUSIC METHODS
    GetSpotipyInfo,
    )
# ININTIALIZE VARIABLES

global title
global artist
global global_context

title = 'Bangarang'
artist = 'Skrillex'
image = 'https://i.scdn.co/image/ab67616d00001e026081278cb62df2757d55633b'
preview = ''

global_context = {}

title_flag = False
artist_flag = False


####################################################################
# MUS PG I


def MusView(request):
    return render(request, 'mus/mus.html')



####################################################################
# SONG_SEARCH PG II


def SongSearch(request, title=title, artist=artist):
    global global_context 
    form = SongSearchForm

    template = 'partials/mus_form.html'
    spotipy = GetSpotipyInfo(title=title, artist=artist)
    print(json.dumps(spotipy, indent=4))

    context = {
        'title': title,
        'artist': artist,
        'image': image,
        'preview': preview,
        'spotipy': spotipy,
        'form': form,
    }


    global_context = context

    return render(request, template, context)


    # spotipy = {
        
    #     'title': title,
    #     'artist': artist,
    #     'data': results,
    #     'items': items,
    #     'title_uri': items[0],
    #     'image': items['images'][0]['url'],
    # }



def SongSearchUpdate(request):

    global title
    global artist

    form = SongSearchForm

    title = request.POST.get('title')
    artist = request.POST.get('artist')

    template = 'partials/mus_form.html'
    spotipy = GetSpotipyInfo(title=title, artist=artist)
    print(json.dumps(spotipy, indent=4))

    context = {
        'title': title,
        'artist': artist,
        'spotipy': spotipy,
        'form': form,
    }

    return render(request, template, context)


    # spotipy = {
        
    #     'title': title,
    #     'artist': artist,
    #     'data': results,
    #     'items': items,
    #     'title_uri': items[0],
    #     'image': items['images'][0]['url'],
    # }



####################################################################
# ANALYZE_SONG RESULTS PG III

def AnalyzeSong(request):
    
    global global_context
    global title
    global artist

    template = 'partials/mus_results.html'

    context = {
        'title': title,
        'artist': artist,
        'global_context': global_context,
    }

    return render(request, template, context)
##################################################
# MISC


