from django.contrib import admin
from dropdown.models import DropdownModel
from dropdown.forms import DropdownModelForm

class DropdownModelAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Date Range', {
            'fields': ('date_range','event',),
            'classes': ('predefined',)
        }),
        (None, {
            'fields': (('start_date', 'end_date'),),
            'classes': ('abcdefg')
        })
    )
    form = DropdownModelForm

    class Media:
        js = ('dropdown/js/base.js',)
admin.site.register(DropdownModel, DropdownModelAdmin)
