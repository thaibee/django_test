from django.shortcuts import render
from django.http import HttpResponse
from news.models import News, Category


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'Cписок новостей',
        'categories': categories
    }
    return render(request, 'news/index.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': category,
        'categories': categories
    }
    return render(request, 'news/category.html', context)
