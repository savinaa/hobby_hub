from django import forms

from hobby_hub.article.models import Articles


class ArticleForm(forms.ModelForm):
    class Meta:
        model=Articles
        fields='__all__'