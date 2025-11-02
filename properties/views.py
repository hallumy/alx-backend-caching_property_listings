from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Properties

@cache_page(60 * 15)
def property_list(request):
    """
    Returns a list of all property records.
    Cached in Redis for 15 minutes to reduce database queries.
    """
    properties = Properties.objects.all()
    data = list(properties)
    return JsonResponse(data, safe=False)

