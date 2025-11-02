from django.core.cache import cache
from properties.models import Property

def get_all_properties():
    """
    Fetch all properties from cache or database.
    Cache the queryset in Redis for 1 hour(3600 seconds) 
    """
    properties = cache.get('all_properties')
    if properties is None:
        Properties = list(Property.objects.all())
        cache.set('all_properties', properties, 3000)
    return properties