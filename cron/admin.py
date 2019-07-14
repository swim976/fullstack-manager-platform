from django.contrib import admin

from cron.models import Log


class LogAdmin(admin.ModelAdmin):
    list_display = ("symbol", "successful", "begin_at", "stdout")
    list_filter = ["symbol"]
    search_fields = ("symbol", "successful", "begin_at")
    list_per_page = 20


admin.site.register(Log, LogAdmin)
