from django import template
register = template.Library()

@register.simple_tag
def category1(lst,j):
    return lst[j]

@register.simple_tag
def category2(lst,j):
    try:
        l = lst[j+1]
    except:
        l = ""
    return l
    