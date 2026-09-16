def get_collection(self, collection_id=None, nav='children', page=None):
    return self.call('collections', {'id': collection_id, 'nav': nav,
        'page': page}, defaults={'id': None, 'nav': 'children', 'page': 1})