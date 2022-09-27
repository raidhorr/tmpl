from django import template


register = template.Library()


CENSOR_WORDS = [
    'ночь', #для проверки
]


@register.filter()
def censor(value):
    """
    выводит 'Х****' вместо цензурированных слов

    value: цензурированные слова
    """
    if type(value) is str:
        for word in CENSOR_WORDS:
            value = value.replace(word, word[0] + "*" * (len(word) - 1))
            value = value.replace(word.capitalize(), word[0] + "*" * (len(word) - 1))
    else:
        raise ValueError('Требуется строка')

    return f'{value}'


@register.simple_tag()
def url_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
       d[k] = v
    return d.urlencoded()


