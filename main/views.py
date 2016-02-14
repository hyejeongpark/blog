from django.shortcuts import render
from django.http import HttpResponse


def index_page(request):
  return HttpResponse('<h1>Home Sweet Home<h1>')

def about_page(request):
  return HttpResponse('<h1>about<h1>')