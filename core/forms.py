from django import forms
from .models import Article


class ArticleInformation(forms.Form):
    article_title = forms.CharField(max_length=100, label='Article Title')
    article_description = forms.CharField(max_length=500, label='Article Description')
    is_publish = forms.BooleanField(label='Is Article Publish?')
    password = forms.CharField(widget=forms.PasswordInput)

    # class Meta:
    #     model = Article
    #     fields = "__all__"