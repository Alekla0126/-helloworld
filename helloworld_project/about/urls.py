#about/urls.py
from django.urls import path
from .views import aboutPageView


urlpatterns = [
    path('', aboutPageView, name="about")
]
