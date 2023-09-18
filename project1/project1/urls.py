"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.first),
    path('index',views.index),
    path('userreg',views.userreg),
    path('contactreg',views.contactreg),
    path('uview',views.uview),
    path('contacview',views.contacview),
    path('login',views.login),
    path('logout',views.logout),
    path('delete/<int:id>',views.delete, name='delete'),
    path('remove/<int:id>',views.remove,name='remove'),
    path('contactedit',views.contactedit),
    path('userpro',views.userpro),
    path('useredi',views.useredi),
    path('adminprofil',views.adminprofil),
    path('updat/<int:id>',views.updat, name='updat'),
    path('updat/updates/<int:id>',views.updates, name='updates'),
    path('updt/<int:id>',views.updt, name='updt'),
    path('updt/contactupdate/<int:id>',views.contactupdate, name='contactupdate'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
