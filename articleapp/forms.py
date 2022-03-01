from django.forms import ModelForm
from django import forms

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    #에디터 커스텀마이징
    content = forms.CharField(widget=forms.Textarea(attrs={"class":"editable text-left","style":"height:auto"}))

    class Meta:
        model = Article
        fields = ["title", "project", "image", "content"]