from django.shortcuts import render
from django.http import HttpResponse
from news.models import News,Category


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'Cписок новостей',
        'categories': categories
    }
    return render(request, 'news/index.html', context)


def get_category(request, categody_id):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Cписок новостей'
    }
    return render(request, 'news/index.html', context)
