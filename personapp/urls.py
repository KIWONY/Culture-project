from django.urls import path

from personapp.views import nice_world

app_name = "personapp"

urlpatterns=[
    path("nice_world/",nice_world, name="nice_world")       #-> person/nice_world로 접속
]