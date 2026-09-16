def to_api_repr(self):
    source_ref = {'projectId': self.source.project, 'datasetId': self.
        source.dataset_id, 'tableId': self.source.table_id}
    configuration = self._configuration.to_api_repr()
    _helpers._set_sub_prop(configuration, ['extract', 'sourceTable'],
        source_ref)
    _helpers._set_sub_prop(configuration, ['extract', 'destinationUris'],
        self.destination_uris)
    return {'jobReference': self._properties['jobReference'],
        'configuration': configuration}