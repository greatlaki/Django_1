from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import *

def index(request):
    bbs = Bb.objects.all()
    return render(request, 'bboard/index.html', {'bbs': bbs})