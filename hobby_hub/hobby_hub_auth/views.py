from django.contrib.auth import login
from django.shortcuts import render

# Create your views here.
from hobby_hub.hobby_hub_auth.forms import SignInForm


def sign_in(req):
    if req.method=='POST':
        form=SignInForm(req.POST)
        if form.is_valid():
            user=authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user:
                login(req,user)
    else:
        form=SignInForm()
    context={
        'form':form,
    }
    return render(req,'auth/sign_in.html',context)