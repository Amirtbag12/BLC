"""
2020 Black
developer : #ABS
"""

# Import all requirements
from .models import Visit
from django.contrib import admin


class VisitAdmin(admin.ModelAdmin):
    list_display = ('ip_address','session_key','visit_count')
    search_fields = ('ip_address',)

admin.site.register(Visit, VisitAdmin)