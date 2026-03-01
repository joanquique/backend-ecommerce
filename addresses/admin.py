from django.contrib import admin
from .models import Address

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "line1", "city", "state", "zip_code", "is_default")
    search_fields = ("user__username", "line1", "city", "state", "zip_code")
    list_filter = ("is_default", "state")