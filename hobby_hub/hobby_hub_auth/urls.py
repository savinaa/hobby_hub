from django.urls import path

from hobby_hub.hobby_hub_auth import views

urlpatterns=[
    path('sign_up/', views.sign_up, name="sign up"),
    path('sign_in/', views.sign_in, name="sign in"),
    path('sign_out/', views.sign_out, name="sign out"),
]