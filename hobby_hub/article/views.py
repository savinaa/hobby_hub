from django.shortcuts import render, redirect

# Create your views here.
from hobby_hub.article.forms import ArticleForm
from hobby_hub.article.models import Articles


def index(req):
    context={
        'articles':Articles.objects.all(),
        'form':ArticleForm(),
    }

    return render(req, 'index.html',context)

def create_article(req):
    form=ArticleForm(req.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    else:
        form=ArticleForm()
    context={
        'form':form,
    }
    return render(req, 'article/create_article.html', context)


