# -*- coding: utf-8 -*-
from django import template

register = template.Library()

def cut(value, arg):
    """
    This cuts out all values of 'arg' from the string!
    """
    
    return value.replace(arg, '')
    
register.filter('cutword', cut)

"""
############################################
# Another way to do this is using decorators
############################################

from django import template

register = template.Library()

@register.filter(name='cutword')
def cut(value, arg):

    return value.replace(arg, '')
"""