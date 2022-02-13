from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args , **kwargs):

        # pk를 가지고 있는 user object 를 user에 담음
        user = User.objects.get(pk=kwargs["pk"])

        # request를 보내는 user와 같은 지 확인
        if not user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated










