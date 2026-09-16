def get_assets(self):
    collection = JSONClientValidated('repository', collection='Asset',
        runtime=self._runtime)
    result = collection.find(self._view_filter()).sort('_id', DESCENDING)
    return objects.AssetList(result, runtime=self._runtime, proxy=self._proxy)