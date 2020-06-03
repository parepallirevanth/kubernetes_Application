# chatapp/urls.py
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views
from django.contrib.auth import views as auth
"""
desc: Calling the list of views of each url from urlpatterns by urls.py everytime 
      webbrowser request
"""

from chat.views import index
urlpatterns = [
    path('', include('frontend.urls')),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('chat/', include('chat.urls', namespace='chat')),
]
