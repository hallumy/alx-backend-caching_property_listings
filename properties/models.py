from django.db import models

class Properties(models.Model):
    """
    Represents properties listing on the platform
    Attributes:
        title (str): The name or title of the property.
        description (str): A detailed text description of the property, its features, or location.
        price_per_night (Decimal): The cost to book the property per night.
        location (str): The city or area where the property is located.
        created_at (datetime): The timestamp when the property was added.
    """
    title       = models.CharField(max_length=200)
    description = models.TextField()
    price       = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2)
    location    = models.CharField(max_length=100)
    created_at  = models.DateTimeField(auto_now_add=True)
