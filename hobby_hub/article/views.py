from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from hobby_hub.article.forms import ArticleForm, EditArticleForm
from hobby_hub.article.models import Article, Like, Dislike


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

    context = {
        'article': article,
        'is_owner':is_owner,
    }
    return render(req, 'article/article_details.html', context)

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


