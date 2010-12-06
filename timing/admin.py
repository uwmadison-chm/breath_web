from models import Run
from django.contrib import admin

class RunAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user']}),
        ('Date', {'fields': ['date']}),
        ('Keypresses', {'fields': ['keypresses']})
        ]
    list_display = ('user', 'date')
    list_filter=['date']
    date_hierarchy = 'date'



admin.site.register(Run, RunAdmin)
