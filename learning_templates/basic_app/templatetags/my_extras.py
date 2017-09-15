from django import template

register=template.Library()

@register.filter(name='cut')

def cut(value, arg):
    '''
    this cuts all values of arg from the
    string
    '''
    return value.replace(arg,'')

#(passAs, func name)
# register.filter('cutString', cut)
