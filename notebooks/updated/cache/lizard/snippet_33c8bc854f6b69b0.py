def get_composition(self, composition_id):
    collection = JSONClientValidated('repository', collection='Composition',
        runtime=self._runtime)
    result = collection.find_one(dict({'_id': ObjectId(self._get_id(
        composition_id, 'repository').get_identifier())}, **self.
        _view_filter()))
    return objects.Composition(osid_object_map=result, runtime=self.
        _runtime, proxy=self._proxy)