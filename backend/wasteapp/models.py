from django.db import models


class WastePickup(models.Model):
    WASTE_TYPES = [
        ("Recyclable", "Recyclable"),
        ("Organic", "Organic"),
        ("General", "General"),
    ]

    name = models.CharField(max_length=100)
    waste_type = models.CharField(max_length=20, choices=WASTE_TYPES)
    pickup_date = models.DateField()
    address = models.TextField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        default="Pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.waste_type}"