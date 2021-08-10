from django.urls import path

from hobby_hub.hobby_hub_auth import views

urlpatterns=[
    path('sign_in/', views.sign_in, name="sign in"),
]