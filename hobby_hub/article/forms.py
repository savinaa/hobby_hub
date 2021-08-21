import os
from os.path import join

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

from hobby_hub import settings
from hobby_hub.article.models import Article
from hobby_hub.core.forms import BootstrapFormMixin


class CreateArticleForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model=Article
        fields='__all__'
        exclude=('user',)

    def clean(self):
        cleaned_data = super().clean()
        value = cleaned_data.get("url")

        try:
            validator = URLValidator()
            validator(value)
        except ValidationError:
            raise ValidationError(f'{value} is not a valid URL !')

        return cleaned_data

class EditArticleForm(CreateArticleForm):
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
