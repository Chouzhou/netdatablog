from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
from django.views.generic import ListView, DetailView

from blog.models import news


def index(request):
    users = User.objects.all()
    for user in users:
        print user.userprofile.desc
    return HttpResponse(users)


class ArticListView(ListView):
    model = news
    template_name = 'artic.html'


class ArticDetailView(DetailView):
    model = news
    template_name = 'artic_detail.html'
