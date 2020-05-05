from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def commentsPageView(request):
    return render(request, 'comments.html', {})
