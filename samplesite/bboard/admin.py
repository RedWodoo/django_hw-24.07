from django.contrib import admin

from .models import Rebenok, Roditel


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'roditel')
    list_display_links = ('title',)
    search_fields = ('title', 'content')


admin.site.register(Rebenok, BbAdmin)
admin.site.register(Roditel)
