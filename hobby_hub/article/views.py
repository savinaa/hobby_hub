from django.shortcuts import render

# Create your views here.
from hobby_hub.article.models import Article


def index(req):
    context={
        'articles':Article.objects.all(),
    }

    return render(req, 'index.html',context)
