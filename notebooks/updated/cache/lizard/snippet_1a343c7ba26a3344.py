def get_collection(self, service_name, collection_name, base_class=None):
    classpath = self.build_classpath(base_class)
    service = self.services.get(service_name, {})
    collections = service.get('collections', {})
    collection_options = collections.get(collection_name, {})
    collection_class = collection_options.get(classpath, None)
    if not collection_class:
        msg = "Collection '{0}' for {1} is not present in the cache."
        raise NotCached(msg.format(collection_name, service_name))
    return collection_class