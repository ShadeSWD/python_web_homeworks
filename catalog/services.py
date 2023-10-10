from config import settings
from django.core.cache import cache


def low_level_cache(queryset, key):
    queryset = queryset
    if settings.CACHE_ENABLED:
        cache_data = cache.get(key)
        if cache_data is None:
            cache_data = queryset
            cache.set(key, cache_data)

        return cache_data

    return queryset
