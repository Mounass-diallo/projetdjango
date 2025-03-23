from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article
from django.urls import reverse_lazy

class ArticleListView(ListView):
    model = Article
    template_name = 'myblog/article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'myblog/article_detail.html'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'myblog/article_form.html'
    fields = ['titre', 'contenu', 'image']

    def form_valid(self, form):
        form.instance.auteur = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'myblog/article_form.html'
    fields = ['titre', 'contenu', 'image']

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'myblog/article_confirm_delete.html'
    success_url = reverse_lazy('article-list')