from django import template
from datetime import datetime, timedelta
from django.utils import timezone

register = template.Library()

@register.filter
def timeSince(datetime):
    now = timezone.now()
    timedelta = now - datetime
    minutes = int(timedelta.seconds / 60)
    return minutes

@register.filter
def formatTime(datetime):
    if datetime == '':
        return '-'
    return datetime.strftime("%Y/%m/%d")

@register.filter
def length(list):
    return len(list)