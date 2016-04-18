# -*- coding:utf-8 -*-
from django import template

register = template.Library()


class UpperNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        context = self.nodelist.render(context)
        return context.lower()


@register.tag
def upper(parser, token):
    nodelist = parser.parse("endupper")  # 设定自定义标签结尾相当于{% endblock%}
    parser.delete_first_token()
    return UpperNode(nodelist)
