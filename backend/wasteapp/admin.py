from django.contrib import admin
from .models import WastePickup


@admin.register(WastePickup)
class WastePickupAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "waste_type",
        "pickup_date",
        "status",
        "created_at",
    )