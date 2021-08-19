from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
from hobby_hub.article.models import Article
from hobby_hub.hobby_hub_auth.forms import SignInForm, SignUpForm, ProfileForm
from hobby_hub.hobby_hub_auth.models import Profile


def sign_up(req):
    if req.POST:
        form=SignUpForm(req.POST)
        if form.is_valid():
            user=form.save()
            login(req,user)
            return redirect('index')
    else:
        form=SignUpForm()
    context={
        'form':form,
    }
    return render(req, 'auth/sign_up.html',context)

def sign_in(req):
    if req.method=='POST':
        form=SignInForm(req.POST)
        if form.is_valid():
            user=form.save()
            login(req,user)
            return redirect('index')
    else:
        form=SignInForm()
    context={
        'form':form,
    }
    return render(req,'auth/accounts/login.html',context)

@login_required
def sign_out(req):
    logout(req)
    return redirect('index')

@login_required
def profile_details(req):
    profile=Profile.objects.get(pk=req.user.id)

    if req.POST:
        form=ProfileForm(req.POST,
                         req.FILES,
                         instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form=ProfileForm(instance=profile)

    user_articles=Article.objects.filter(user_id=req.user.id)
    context={
        'form':form,
        'articles':user_articles,
        'profile':profile,
    }
    return render(req, 'auth/accounts/user_profile.html',context)