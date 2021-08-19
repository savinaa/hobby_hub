from django import forms

from hobby_hub.article.models import Article
from hobby_hub.common.models import Comment


class CommentForm(forms.ModelForm):
    article_pk=forms.IntegerField(
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Comment
        fields=('text','article_pk')

    def save(self,comit=True):
        article_pk=self.cleaned_data['article_pk']
        article=Article.objects.get(pk=article_pk)
        comment=Comment(
            text=self.cleaned_data['text'],
            article=article,
        )

        if comit:
            comment.save()
        return comment