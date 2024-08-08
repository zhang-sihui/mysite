import json
from django.conf import settings


def translate_message(msg, where='code'):
    """
    msg: 要翻译的字符串
    where: 字符串所属文件 code: python 文件, html: html 文件 
    """
    message = str(msg)
    try:
        translations = settings.TRANSLATIONS_DATA
        if translations:
            message = translations[where].get(msg, msg)
    except Exception as e:
        pass
    return message
