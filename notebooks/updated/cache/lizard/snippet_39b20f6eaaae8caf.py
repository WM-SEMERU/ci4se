def get_relationships_for_source(self, source_id):
    collection = JSONClientValidated('relationship', collection=
        'Relationship', runtime=self._runtime)
    result = collection.find(dict({'sourceId': str(source_id)}, **self.
        _view_filter())).sort('_sort_id', ASCENDING)
    return objects.RelationshipList(result, runtime=self._runtime)