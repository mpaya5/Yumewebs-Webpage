from django import template
from portfolio.models import Work

register = template.Library()

@register.simple_tag
def get_work_list():
    works = Work.objects.all()
    return works