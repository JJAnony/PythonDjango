from django.contrib import admin
from core.models import Event


# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'event_date', 'created_date')
    list_filter = ('event_date', 'user',)


admin.site.register(Event, EventAdmin)
