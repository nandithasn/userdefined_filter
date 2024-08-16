from django import template
register=template.Library()


def swap(value):
    return value.swapcase()


register.filter('swapping',swap)



def replace(value,r):
    return value.replace(r,'A')
register.filter('replace',replace)