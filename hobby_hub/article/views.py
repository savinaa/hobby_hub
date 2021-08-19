from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from hobby_hub.article.forms import ArticleForm, EditArticleForm
from hobby_hub.article.models import Article, Like, Dislike
from hobby_hub.common.forms import CommentForm
from hobby_hub.common.models import Comment
from hobby_hub.core.views import PostOnlyView


def index(req):
    context={
        'articles':Article.objects.all(),
        'form':ArticleForm(),
    }
    return render(req, 'index.html',context)

def article_details(req,pk):
    article = Article.objects.get(pk=pk)
    article.likes_count = article.like_set.count()
    article.dislikes_count = article.dislike_set.count()
    is_owner=article.user==req.user

    is_liked_by_user=article.like_set.filter(user_id=req.user.id).exists()
    is_disliked_by_user=article.dislike_set.filter(user_id=req.user.id).exists()

    comment_form=CommentForm(
        initial={
            'article_pk': article.id,
        }
    )

    context = {
        'article': article,
        'is_owner':is_owner,
        'is_liked':is_liked_by_user,
        'is_disliked':is_disliked_by_user,
        'comments':article.comment_set.all(),
        'comment_form':comment_form,
    }
    return render(req, 'article/article_details.html', context)

@login_required
def article_like(req, pk):
    article = Article.objects.get(pk=pk)
    like_obj = article.like_set.filter(user_id=req.user.id).first()
    if like_obj:
        like_obj.delete()
    else:
        like=Like(
            article=article,
            user=req.user,
        )
        like.save()
    return redirect('article details',pk)

@login_required
def article_dislike(req, pk):
    article = Article.objects.get(pk=pk)
    dislike_obj = article.dislike_set.filter(user_id=req.user.id).first()
    if dislike_obj:
        dislike_obj.delete()
    else:
        dislike = Dislike(
            article=article,
            user=req.user,
        )
        dislike.save()

    return redirect('article details',pk)

class CommentArticleView(LoginRequiredMixin, PostOnlyView):
    form_class = CommentForm

    def form_valid(self, form):
        article = Article.objects.get(pk=self.kwargs['pk'])
        comment = Comment(
            text=form.cleaned_data['text'],
            article=article,
            user=self.request.user,
        )
        comment.save()

        return redirect('article details', article.id)

    def form_invalid(self, form):
        pass

@login_required
def create_article(req):
    if req.method=='POST':
        form=ArticleForm(req.POST, req.FILES)
        if form.is_valid():
            article=form.save(commit=False)
            article.user=req.user
            article.save()
            return redirect('index')
    else:
        form=ArticleForm()
    context={
        'form':form,
    }
    return render(req, 'article/create_article.html', context)

@login_required
def edit_article(req,pk):
    article= Article.objects.get(pk=pk)
    if req.method=='POST':
        form=EditArticleForm(req.POST, req.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=EditArticleForm(instance=article)
    context={
        'form':form,
        'article':article,
    }
    return render(req, 'article/article_edit.html', context)

@login_required
def delete_article(req,pk):
    article = Article.objects.get(pk=pk)
    if req.method=='POST':
        article.delete()
        return redirect('index')
    else:
        context={
            'article':article,
        }
        return render(req,'article/article_delete.html',context)


