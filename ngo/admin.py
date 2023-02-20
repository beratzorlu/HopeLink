from django.contrib import admin
from .models import NGO, FocusArea


# Register your models here.
class NGOAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = ('name',)


class FocusAreaAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = ('name',)


admin.site.register(NGO, NGOAdmin)
admin.site.register(FocusArea, FocusAreaAdmin)
