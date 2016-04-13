# coding = utf-8
from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from blog.models import news, UserProfile


class ProfileInline(admin.StackedInline):
    model = UserProfile
    verbose_name = 'profile'


class UserAdmin(admin.ModelAdmin):
    inlines = (ProfileInline,)


admin.site.register(news)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
