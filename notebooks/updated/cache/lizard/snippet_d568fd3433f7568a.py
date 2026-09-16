def create_cache(name):
    caches = {subclass.name(): subclass for subclass in Cache.__subclasses__()}
    return caches.get(name, NaiveCache)()