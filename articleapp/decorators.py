
from django.http import HttpResponseForbidden

from articleapp.models import Article



def article_ownership_required(func):
    def decorated(request, *args , **kwargs):

        # pk를 가지고 있는 Article object 를 article에 담음 / import
        article = Article.objects.get(pk=kwargs["pk"])

        # request를 보내는 user와 같은 지 확인
        if not article.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated










