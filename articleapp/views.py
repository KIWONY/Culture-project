from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView

from articleapp.decorators import article_ownership_required
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article


@method_decorator(login_required,"get")
@method_decorator(login_required,"post")
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = "articleapp/create.html"

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    #self.object로 완성된 게시글 객체에 접근 -> 해당 pk를 불러와서, pk를 통해 ArticleDetailView로 연결
    def get_success_url(self):
        return reverse("articleapp:detail", kwargs ={"pk" : self.object.pk})

class ArticleDetailView(DetailView):
    model = Article
    context_object_name = "target_article"
    template_name = "articleapp/detail.html"


@method_decorator(article_ownership_required,"get")
@method_decorator(article_ownership_required,"post")
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreationForm
    context_object_name = "target_article"
    template_name = "articleapp/update.html"

    def get_success_url(self):
        return reverse("articleapp:detail", kwargs ={"pk" : self.object.pk})



@method_decorator(article_ownership_required,"get")
@method_decorator(article_ownership_required,"post")
class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "articleapp/delete.html"
    context_object_name = "target_article"
    success_url = reverse_lazy("articleapp:list")

class ArticleListView(ListView):
    model = Article
    template_name = "articleapp/list.html"
    context_object_name = "article_list"
    paginate_by = 9    #페이지에 몇개까지 보여줄 것인가







