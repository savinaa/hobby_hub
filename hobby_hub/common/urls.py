from django.urls import path

from hobby_hub.common.views import LandingPage

urlpatterns=[
    path('', LandingPage.as_view(), name='index'),
]