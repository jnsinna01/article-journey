from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import Article, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect


class SearchResultsList(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'search.html'
    login_url = 'login'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Article.objects.filter(title__icontains=query)


def likeview(request, pk):
    article = get_object_or_404(Article, id=request.POST.get('article_pk'))
    article.likes.add(request.user)
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'create_article.html'
    fields = ('title', 'image', 'body',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'create_comment.html'
    fields = ('article', 'comment',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    ordering = ['-date']
    template_name = 'list_article.html'
    login_url = 'login'


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'detail_article.html'
    login_url = 'login'


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = 'update_article.html'
    fields = ('title', 'image', 'body',)
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'delete_article.html'
    login_url = 'login'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


