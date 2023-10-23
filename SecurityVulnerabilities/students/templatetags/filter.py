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