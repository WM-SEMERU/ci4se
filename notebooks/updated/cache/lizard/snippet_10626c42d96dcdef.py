def get_grade_system(self, grade_system_id):
    collection = JSONClientValidated('grading', collection='GradeSystem',
        runtime=self._runtime)
    result = collection.find_one(dict({'_id': ObjectId(self._get_id(
        grade_system_id, 'grading').get_identifier())}, **self._view_filter()))
    return objects.GradeSystem(osid_object_map=result, runtime=self.
        _runtime, proxy=self._proxy)