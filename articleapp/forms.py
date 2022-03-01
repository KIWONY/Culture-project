from django.forms import ModelForm
from django import forms

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    #에디터 커스텀마이징
    content = forms.CharField(widget=forms.Textarea(attrs={"class":"editable text-left","style":"height:auto"}))

    #foreignkey선택 시 선택하지 않아도 되게
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)
    class Meta:
        model = Article
        fields = ["title", "project", "image", "content"]