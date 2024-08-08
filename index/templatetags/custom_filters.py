from django import template
from ..common import translate_message

register = template.Library()


@register.filter
def translate_str(msg):
    """ 通过管道实现模板内容翻译 """
    message = translate_message(msg, 'html')
    return message
