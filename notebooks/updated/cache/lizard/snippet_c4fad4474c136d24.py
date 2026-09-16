def _save(self):
    collection = JSONClientValidated('assessment', collection=
        'AssessmentTaken', runtime=self._runtime)
    collection.save(self._my_map)