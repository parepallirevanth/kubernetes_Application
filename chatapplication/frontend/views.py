from django.shortcuts import render

from .models import chat

# Create your views here.
def index(request):
    """
    Desc:Functions used call the homepage
    params: Http request
    return: redirects to homepage
    """
    return render(request,'chat/index.html')