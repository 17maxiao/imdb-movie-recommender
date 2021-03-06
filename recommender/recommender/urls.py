"""recommender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from main.views import home, login_view, signin, signup, shelf, results, search, addtoshelf, entry, genrerec, shelfrec, cleargenres

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login', login_view, name='login_view'),
    path('signin', signin, name='signin'),
    path('signup', signup, name='signup'),
    path('shelf', shelf, name='shelf'),
    path('search', search, name='search'),
    path('genrerec', genrerec, name='genrerec'),
    path('cleargenres', cleargenres, name='cleargenres'),
    path('shelfrec', shelfrec, name='shelfrec'),
    path('addtoshelf/<str:title>', addtoshelf, name='addtoshelf'),
    path('entry/<str:id>', entry, name='entry'),
]
