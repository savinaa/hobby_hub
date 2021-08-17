from django.shortcuts import render, redirect

# Create your views here.
from hobby_hub.article.forms import ArticleForm, EditArticleForm
from hobby_hub.article.models import Article


def index(req):
    context={
        'articles':Article.objects.all(),
        'form':ArticleForm(),
    }

    return render(req, 'index.html',context)

def create_article(req):
    if req.method=='POST':
        form=ArticleForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
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
    return render(req, 'article/edit_article.html', context)


