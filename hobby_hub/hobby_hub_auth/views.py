from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
from hobby_hub.hobby_hub_auth.forms import SignInForm, SignUpForm


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