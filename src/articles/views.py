from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .forms import ArticleForm
from .models import Article

# def article_list_view(request):
#     queryset = Article.objects.all()
#     context = {
#         "object_list": queryset
#     }
#     return render(request, "articles/article_list.html", context)

# def article_detail_view(request, id):
#     obj = get_object_or_404(Article, id=id)
#     context = {
#         "object": obj
#     }
#     return render(request, "articles/article_detail.html", context)

# articles/<modelname>_list.html
class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()