def get_items(self, collection_uri):
    cname = os.path.split(collection_uri)[1]
    return self.search_metadata('collection_name:%s' % cname)