# -*- coding: utf-8 -*-
import functools
import json
import string

from django.shortcuts import HttpResponse

from blog.models import News

pagesize = 5


def obj_serialize(event, fields_list):
    e = {}
    for field in fields_list:
        e[field] = '%s' % getattr(event, field)
    return e


def http_response(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        ret = fn(*args, **kwargs)
        return HttpResponse(json.dumps(ret, ensure_ascii=False))

    # 这是Unicode，你可以给dump函数加个参数，ensure_ascii，如果你要缩进什么的，可以用indent参数
    return wrapper


@http_response
def index(req):
    # page = string.atoi(req.Get.get('page', '0'))
    news_objs = News.objects.filter(news_body__contains="政府",
                                    news_time__gt="150500")  # .distinct().values('news_body').order_by('news_time')
    # 过滤新闻主题是否包含有政府,时间是否大于150500
    # return HttpResponse(json.dumps(news_objs))
    return [obj_serialize(news_obj, getattr(news_obj, 'list_field')) for news_obj in news_objs]  # 列表推导将数据用列表的形式输出
    # list_field与models中的News里面的要一致
