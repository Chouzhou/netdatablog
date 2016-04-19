"""netdatablog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog.views import ArticListView, login, register, add_new, modify_new, ArticDetailView, review_detail, add_review, \
    search_new

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^add_new/$', add_new, name='add_new'),
    url(r'^modify_new/$', modify_new, name='modify_new'),
    url(r'^review_detail/$', review_detail, name='review_detail'),
    url(r'^add_review/$', add_review, name='add_review'),
    url(r'^search_new/$', search_new, name='search_new'),
    url(r'^list/$', ArticListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', ArticDetailView.as_view(), name='detail'),
]
