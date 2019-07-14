from django.contrib import admin

from people.models import People


class PeopleAdmin(admin.ModelAdmin):
    list_display = ("name", "relation", "beta")
    list_filter = ("familiar",)
    search_fields = ("name", "pinyin", "relation", "familiar", "beta")
    list_editable = ("beta",)
    ordering = ("familiar",)
    list_per_page = 20


admin.site.register(People, PeopleAdmin)
