from django.urls import path
# from articles.views import article_list_view, article_detail_view
from .views import ArticleListView, ArticleDetailView, ArticleCreateView

app_name = 'articles'
urlpatterns = [
    # path('', article_list_view, name='article-list'),
    # path('<int:id>/', article_detail_view, name='article-detail'),
    path('', ArticleListView.as_view(), name='article-list'),
    # the default to look for is pk(primary key) or slug & not id
    # path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),

]