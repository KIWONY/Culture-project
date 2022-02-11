from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from personapp.views import nice_world, AccountCreateView

app_name = "personapp"

urlpatterns=[
    path("nice_world/",nice_world, name="nice_world"),                  #함수형 , -> person/nice_world로 접속

    #jango에 있는 기본 user import.view에서 따로 작성 불필요

    path("login/", LoginView.as_view(template_name="personapp/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path("create/", AccountCreateView.as_view(), name="create"),          #class형 , 회원가입 경로

]