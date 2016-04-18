# -*- coding: utf-8 -*-
# from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import Permission
# Create your views here.
from django.views.generic import ListView, DetailView
import uuid
from blog.models import News, User
from django import forms


# def index(request):
#     users = User.objects.all()
#     for user in users:
#         print user.userprofile.desc
#     return HttpResponse(users)
# 自定义form表单项
class LoginForm(forms.Form):
    email = forms.CharField(label="email", max_length=100)
    pwd = forms.CharField(label="password", widget=forms.PasswordInput)


class ArticListView(ListView):
    model = News  # 要显示详情内容的类
    template_name = 'artic.html'  # 模板名称，默认为 应用名/类名_detail.html（即 app/modelname_detail.html）

    # def get_context_data(self, **kwargs):
    #     context = super(ArticListView, self).get_context_data(**kwargs)
    #     return context


class ArticDetailView(DetailView):
    model = News
    template_name = 'artic_detail.html'


def login(request):
    if ('email' or 'pwd') not in request.GET:
        lf = LoginForm()
        return render_to_response('login.html', {'lf': lf, 'custom_name': 'sliver'})

    lf = LoginForm(request.GET)
    email = lf.data['email']
    pwd = lf.data['pwd']
    # 判断用户是否存在
    try:
        user = User.objects.get(email=email)
        # 将从数据库里面找到的数据存于session中
        request.session['email'] = email
        request.session['pwd'] = pwd
    except User.DoesNotExist:
        pass
    else:
        if user.check_password(pwd):
            if user.has_perm("blog.can_view"):
                # do something
                return HttpResponse("You can see news")
            return HttpResponse("You can not see news")
    return HttpResponseRedirect("/blog/login")


def register(request):
    if ('email' or 'pwd') not in request.GET:
        lf = LoginForm()
        return render_to_response('register.html', {'lf': lf})
    lf = LoginForm(request.GET)
    email = lf.data['email']
    pwd = lf.data['pwd']
    user = User()
    user.username = uuid.uuid1()
    user.email = email
    user.set_password(pwd)
    user.desc = 'lazy'
    user.save()
    user.user_permissions = [Permission.objects.get(name='Can see news'), Permission.objects.get(name='Can edit news')]
    return HttpResponseRedirect("/blog/login/")


# 添加新闻
def add_new(request):
    new = News(news_thread='天津',
               news_title='天津塘沽爆炸',
               news_url='http://new.sina.com/20150802/4321',
               news_time='2015-08-02 19:30',
               news_body='塘沽爆炸导致腾讯机房故障'
               )
    # 第一种方法创建
    # new.news_from = 'aa'
    new.save()
    return HttpResponse('success')
    # 查找新闻并修改


def modify_new(request):
    new = News.objects.get(news_url='http://new.sina.com/20150802/4321')
    if not new:
        return HttpResponse('fail')
    new.news_body = '今天没吃药'
    new.save()
    return HttpResponse('success')
