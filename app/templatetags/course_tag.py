from django import template
import math

register = template.Library()

@register.simple_tag
def get_discount_price(price,discount):
        
        if discount is None or discount is 0:
            return price 
        else:
            sellprice =price - (price * (discount/100))
            return math.floor(sellprice)