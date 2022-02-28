from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required,"get")
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("projectapp:detail", kwargs={"pk":self.request.GET.get("project_pk")})

    def get(self, request, *args, **kwargs):

        #project_pk를 가진 project가 없으면 404페이지를 response한다.
        project = get_object_or_404(Project, pk=self.request.GET.get("project_pk"))
        user = self.request.user

        #구독정보를 찾음
        subscription = Subscription.objects.filter(user=user, project=project)

        #이미 구독이 되어있다면
        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()

        return super(SubscriptionView, self).get(request,*args,**kwargs)

#구독한 articles 가져오기
class SubscriptionListView(ListView):
    model = Article
    context_object_name = "article_list"
    template_name = "subscribeapp/list.html"
    paginate_by = 5

    def get_queryset(self):
        #user가 구독한 project찾기(구독정보를 모두 가져온 후 project에 해당하는 값들을 list화.
        projects = Subscription.objects.filter(user=self.request.user).values_list("project")

        # field lookups 사용
        article_list= Article.objects.filter(project__in=projects)

        return article_list
















