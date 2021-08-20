import os
from os.path import join

from django import forms

from hobby_hub import settings
from hobby_hub.article.models import Article
from hobby_hub.core.forms import BootstrapFormMixin


class ArticleForm(BootstrapFormMixin,forms.ModelForm):
    class Meta:
        model=Article
        fields='__all__'
        exclude=('user',)

class EditArticleForm(ArticleForm):
    def save(self, commit=True):
        db_article=Article.objects.get(pk=self.instance.id)
        if commit:
            os.remove(join(settings.MEDIA_ROOT,str(db_article.image)))
        return super().save(commit)

    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }
            )
        }
