from django.urls import path
from .views import *


urlpatterns = [
    path('new/', ArticleCreateView.as_view(), name='article_create'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('<int:pk>/like/', likeview, name='article_like'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='article_comment'),
    path('', ArticleListView.as_view(), name='article_list'),
]