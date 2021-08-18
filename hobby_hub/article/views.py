from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from hobby_hub.article.forms import ArticleForm, EditArticleForm
from hobby_hub.article.models import Article, Like


def index(req):
    context={
        'articles':Article.objects.all(),
        'form':ArticleForm(),
    }
    return render(req, 'index.html',context)

def article_details(req,pk):
    article = Article.objects.get(pk=pk)
    article.likes_count = article.like_set.count()
    is_owner=article.user==req.user

    context = {
        'article': article,
        'is_owner':is_owner,
    }
    return render(req, 'article/article_details.html', context)

def url_to_article_like_id(req,pk):
    article = Article.objects.get(pk=pk)
    like=Like(
        article=article,
    )
    like.save()
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


