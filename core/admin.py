from django.contrib import admin
from .models import CodingStat

@admin.register(CodingStat)
class CodingStatAdmin(admin.ModelAdmin):
    list_display = ("platform", "problems_solved", "rating")
    search_fields = ("platform",)