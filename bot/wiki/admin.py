from django.contrib import admin

from .models import Location


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        "date_created",
        "name",
        "description",
    )
    search_fields = ("name",)
    list_filter = ("date_created",)
    empty_value_display = "-пусто-"


admin.site.register(Location, LocationAdmin)
