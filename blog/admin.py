# -*- coding: utf-8 -*-
# 需要这样写coding格式
from django.contrib import admin
# from django.contrib.auth.models import User

# Register your models here.
from blog.models import News, User  # , UserProfile

'''
class ProfileInline(admin.StackedInline):
    model = UserProfile
    verbose_name = 'profile'



class UserAdmin(admin.ModelAdmin):
    inlines = (ProfileInline,)
'''
admin.site.register(User)
admin.site.register(News)
'''
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# 需要取消注册之后才能重新注册User,不然会报错
'''
