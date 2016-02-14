from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from main.models import Article

def index_page(request):
    return HttpResponse('<h1>Home Sweet Home</h1>')

def about_page(request):
    return HttpResponse('<h1>about</h1>')

class ArticleListView(ListView):
    model = Article
