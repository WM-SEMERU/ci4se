def handle(self, *args, **options):
    models.Observer.objects.all().delete()
    models.Subscriber.objects.all().delete()
    for cache_key in cache.keys(search='{}*'.format(THROTTLE_CACHE_PREFIX)):
        cache.delete(cache_key)