from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from main.models import Article

def index_page(request):
    return HttpResponse('<h1>Home Sweet Home</h1>')

def about_page(request):
    return HttpResponse('<h1>about</h1>')

class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    ordering = '-id'

class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
