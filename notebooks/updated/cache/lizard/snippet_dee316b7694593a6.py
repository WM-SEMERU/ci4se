def get_objective(self, objective_id):
    collection = JSONClientValidated('learning', collection='Objective',
        runtime=self._runtime)
    result = collection.find_one(dict({'_id': ObjectId(self._get_id(
        objective_id, 'learning').get_identifier())}, **self._view_filter()))
    return objects.Objective(osid_object_map=result, runtime=self._runtime,
        proxy=self._proxy)