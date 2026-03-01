from django.db import models
from orders.models import Order

class Payment(models.Model):
    PROVIDER_CHOICES = [
        ("cash", "Cash"),
        ("card", "Card"),
        ("mp", "MercadoPago"),
    ]
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="payment")
    provider = models.CharField(max_length=20, choices=PROVIDER_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Order #{self.order.id}"