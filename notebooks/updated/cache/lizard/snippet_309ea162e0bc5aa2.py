def get_assessments(self):
    collection = JSONClientValidated('assessment', collection='Assessment',
        runtime=self._runtime)
    result = collection.find(self._view_filter()).sort('_id', DESCENDING)
    return objects.AssessmentList(result, runtime=self._runtime, proxy=self
        ._proxy)