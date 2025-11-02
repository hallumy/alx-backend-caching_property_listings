from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Properties
from properties.utils import get_all_properties

@cache_page(60 * 15)
def property_list(request):
    """
    Returns a list of all property records.
    Cached in Redis for 15 minutes to reduce database queries.
    """
    properties = get_all_properties()
    return JsonResponse({"properties: list(properties)"}, safe=False)

