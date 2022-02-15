from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from profileapp.models import Profile


def profile_ownership_required(func):
    def decorated(request, *args , **kwargs):

        # pk를 가지고 있는 user object 를 user에 담음
        profile = Profile.objects.get(pk=kwargs["pk"])

        # request를 보내는 user와 같은 지 확인
        if not profile.user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated










