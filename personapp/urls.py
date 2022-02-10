from django.urls import path

from personapp.views import nice_world, AccountCreateView

app_name = "personapp"

urlpatterns=[
    path("nice_world/",nice_world, name="nice_world"),                  #함수형 , -> person/nice_world로 접속
    path("create/", AccountCreateView.as_view(), name="create"),          #class형 , 회원가입 경로
]