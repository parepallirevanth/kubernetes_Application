from django.urls import path

from  . import views
"""
desc: Calling the list of views of each url from urlpatterns by urls.py everytime 
      webbrowser request
input:Path(index)
return: views of each url
"""
urlpatterns = [
    path('', views.index,name='index'),

]