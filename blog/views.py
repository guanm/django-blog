from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from . import models


def index(request):
    # return HttpResponse('Hello')
    # return render(request, 'blog/index.html', {'hello': 'hello blog'})
    # article = models.Article.objects.get(pk=1)
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})


def edit_action(request):
    title = request.POST.get('title', 'Title')
    content = request.POST.get('content', 'CONTENT')
    models.Article.objects.create(title=title, content=content)

    article_id = request.POST.get('article_id', '0')
    if article_id == '0':
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'blog/article_page.html', {'article': article})