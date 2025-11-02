from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property
from properties.utils import get_all_properties

@cache_page(60 * 15)
def property_list(request):
    """
    Return all properties as JSON using low-level cache for 1 hour.
    """
    properties = get_all_properties()
    return JsonResponse({"properties: list(properties)"}, safe=False)

