from django.contrib import admin
from schedule.models import Calendar, Event, CalendarRelation, Rule

class CalendarAdminOptions(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name']
    list_display = ('name', 'slug')

class EventAdminOptions(admin.ModelAdmin):
    list_display = ('start', 'end', 'title', 'calendar', 'creator')
    list_display_links = ('start', 'title')
    search_fields = ('title', 'description')
    list_filter = ('start','calendar','creator')
    radio_fields = {'calendar':admin.HORIZONTAL, 'rule': admin.HORIZONTAL}

admin.site.register(Calendar, CalendarAdminOptions)
admin.site.register(Event, EventAdminOptions)
admin.site.register([Rule, CalendarRelation])
