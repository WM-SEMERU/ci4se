def get_collections(self):
    collections = self.request.matchdict['collections'].split('/')[0]
    collections = [coll.strip() for coll in collections.split(',')]
    return set(collections)