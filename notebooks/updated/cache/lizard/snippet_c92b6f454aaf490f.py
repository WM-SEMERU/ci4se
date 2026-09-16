def get_assessment(self, assessment_id):
    collection = JSONClientValidated('assessment', collection='Assessment',
        runtime=self._runtime)
    result = collection.find_one(dict({'_id': ObjectId(self._get_id(
        assessment_id, 'assessment').get_identifier())}, **self._view_filter())
        )
    return objects.Assessment(osid_object_map=result, runtime=self._runtime,
        proxy=self._proxy)