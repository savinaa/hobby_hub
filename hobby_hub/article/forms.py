from django import forms

from hobby_hub.article.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields='__all__'