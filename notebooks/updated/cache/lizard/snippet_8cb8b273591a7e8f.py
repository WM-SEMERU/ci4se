def get_items(self):
    collection = JSONClientValidated('assessment', collection='Item',
        runtime=self._runtime)
    result = collection.find(self._view_filter()).sort('_id', DESCENDING)
    return objects.ItemList(result, runtime=self._runtime, proxy=self._proxy)