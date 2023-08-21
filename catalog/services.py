from django.conf import settings
from django.core.cache import cache

from catalog.models import Version


def cache_version(version_pk):
    if settings.CACHE_ENABLED:
        key = cache.get(f'version_list{version_pk}')
        version_list = cache.get(key)
        if version_list is None:
            version_list = Version.objects.filter(version_pk=version_pk)
            cache.set(key, version_list)
    else:
        version_list = Version.objects.filter(version_pk=version_pk)

    return version_list
