from django import template


register = template.Library()


CURRENCIES_SYMBOLS = {
   'rub': '',
   'usd': '$',
}


@register.filter()
def currency(value, code='rub'):
    """
    value: значение, к которому нужно применить фильтр
    code: код валюты
    """
    postfix = CURRENCIES_SYMBOLS[code]

    return f'{value} {postfix}'


@register.simple_tag()
def current_time(format_string='%b %d %Y'):
    return datetime.utcnow().strftime(format_string)
