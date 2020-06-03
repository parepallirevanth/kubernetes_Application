#importing required modules
from django.urls import path,include
from django.conf import settings 
from  . import views
from django.conf.urls.static import static 
  

"""
desc: Calling the list of views of each url from urlpatterns by urls.py everytime 
      webbrowser request
input:Path(index,register,login,logout,activate/<token>)
return: views of each url
"""
urlpatterns = [
     path('index', views.index,name='index'),
     path("register", views.register,name="register"),
     path("login",views.login,name="login"),
     path("logout",views.logout,name="logout"),
     path('activate/<token>',views.activate, name='activate'),
     
 ]