# Generated by Django 3.0.7 on 2021-03-10 17:05
from calendar import monthrange

from django.db import migrations
from django.utils import timezone


def generate_expiring_date(p2s):
    year = p2s.start_date.year
    month = p2s.start_date.month
    if p2s.periodicity == "month":
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1
    elif p2s.periodicity == "year":
        year += 1
    else:
        raise ValueError(f'periodicity = "{p2s.periodicity}" not supported!')

    last_day_of_month = monthrange(year, month)[1]
    if p2s.start_day > last_day_of_month:
        day = last_day_of_month
    else:
        day = p2s.start_day
    return p2s.start_date.replace(year, month, day)


def update_expiring_date(p2s):
    if p2s.subscription.is_default:
        p2s.expiring_date = generate_expiring_date(p2s)
    elif p2s.is_grace_period:
        p2s.expiring_date = p2s.start_date + timezone.timedelta(days=p2s.grace_period)
    else:
        p2s.expiring_date = generate_expiring_date(p2s)


def set_start_day(apps, schema):
    ProjectSubscription = apps.get_model('payment_system', 'ProjectSubscription')
    for p2s in ProjectSubscription.objects.all():
        p2s.start_day = p2s.start_date.day
        update_expiring_date(p2s)
        p2s.save()


class Migration(migrations.Migration):

    dependencies = [
        ('payment_system', '0039_auto_20210310_1554'),
    ]

    operations = [
        migrations.RunPython(
            code=set_start_day,
            reverse_code=migrations.RunPython.noop,
        ),
    ]