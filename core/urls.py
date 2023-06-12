from django.urls import path
from core.views import *
from django.views.generic import RedirectView
urlpatterns = [
    path("", RedirectView.as_view(url="home/")),
    path('home/', CoreHome.as_view(), name="core_home")
]
