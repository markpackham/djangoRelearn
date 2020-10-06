from django.shortcuts import render, get_object_or_404, redirect
from .forms import ArticleForm
from .models import Article

def article_list_view(request):
    queryset = Article.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "articles/article_list.html", context)

def article_detail_view(request, id):
    obj = get_object_or_404(Article, id=id)
    context = {
        "object": obj
    }
    return render(request, "articles/article_detail.html", context)