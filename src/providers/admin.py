from django.contrib import admin

from .models import Provider

class ProviderAdmin(admin.ModelAdmin):
    list_display = ("id_uuid", "id", "first_name", "last_name", "sex", "birth_date", "rating", "company", "active", "country", "language")
    list_filter = ("sex", "active", "country", "language")
    search_fields = ("first_name", "last_name", "company")
    fields = ("id_uuid", "id", "first_name", "last_name", "sex", "birth_date", "rating", "primary_skills", "secondary_skill", "company", "active", "country", "language")

admin.site.register(Provider, ProviderAdmin)