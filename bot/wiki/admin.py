from django.contrib import admin

from .models import Location, District, Adjacent_district, Picture, Category


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        "date_created",
        "name",
        "description",
        "category",
        "picture",
    )
    search_fields = ("name",)
    list_filter = ("date_created",)
    empty_value_display = "-пусто-"


class DistrictAdmin(admin.ModelAdmin):
    list_display = (
        "date_created",
        "name",
        "adjacent_district",
    )
    search_fields = ("name",)
    list_filter = ("date_created",)
    empty_value_display = "-пусто-"


class Adjacent_districtAdmin(admin.ModelAdmin):
    list_display = (
        "main_district",
        "neighboring_district",
    )
    search_fields = ("main_district", "neighboring_district")
    empty_value_display = "-пусто-"


class PictureAdmin(admin.ModelAdmin):
    list_display = (
        "date_created",
        "name",
        "image",
    )
    search_fields = ("name",)
    list_filter = ("date_created",)
    empty_value_display = "-пусто-"


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "date_created",
        "name",
    )
    search_fields = ("name",)
    list_filter = ("date_created",)
    empty_value_display = "-пусто-"


admin.site.register(Location, LocationAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Adjacent_district, Adjacent_districtAdmin)
admin.site.register(Picture, PictureAdmin)
admin.site.register(Category, CategoryAdmin)
