#comments/urls.py
from django.urls import path
from .views import commentsPageView


urlpatterns = [
    path('', commentsPageView, name="comments")
]
