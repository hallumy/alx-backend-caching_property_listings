from django.core.cache import cache
from properties.models import Property
from django_redis import get_redis_connection
import logging

logger = logging.getLogger(__name__)


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

def get_redis_cache_metrics():
    """
    Retrieve Redis cache hit/miss metrics and calculate hit ratio
    """
    try:
        redis_conn = get_redis_connection("default")
        info = redis_conn.info("status")
        hits = info.get("keyspace_hits", 0)
        misses = info.get("keyspace_missess", 0)

        total_requests = hits + misses
        hit_ratio = (hits / total_requests) if total_requests> 0 else 0

        metrics = { 
            "keyspace_hits": hits,
            "keyspace_misses": misses,
            "hit_ratio": hit_ratio
        }
        logger.info(f"Redis Cache Metrics: {metrics}")
    except:
        logger.error(f"Failed to retrieve Redis metrics: {e}") 
    return metrics