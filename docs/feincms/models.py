#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
integrate django-schedule with feincms

see http://github.com/matthiask/feincms/
"""
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.template.loader import render_to_string
from feincms.module.page.models import Page
import datetime
from schedule.models import Event, Calendar
from schedule.periods import weekday_names, Month, Week, Day


class EventContent(models.Model):
    event = models.ForeignKey(Event)

    class Meta:
        abstract = True
        verbose_name = _(u'Event')
        verbose_name_plural = _(u'Events')

    def render(self, **kwargs):
        return render_to_string('content/schedule/event.html', { 'event':self.event })

class CalendarContent(models.Model):
    calendar = models.ForeignKey(Calendar)

    class Meta:
        abstract = True
        verbose_name = _(u'Calendar')
        verbose_name_plural = _(u'Calendars')

    def render(self, **kwargs):
        date = datetime.datetime.now()
        event_list = self.calendar.event_set.all()
        periods = {'month':Month, 'week':Week, 'day':Day}
        period_objects = dict([(period.__name__.lower(), period(event_list, date)) for period in periods])
        return render_to_string('content/schedule/calendar.html', {
                'date': date,
                'periods': period_objects,
                'calendar': self.calendar,
                'weekday_names': weekday_names,
        })


Page.create_content_type(EventContent, POSITION_CHOICES=(
    ('right', _(u'right')),
    ('center', _(u'center')),
    ))

Page.create_content_type(CalendarContent)
