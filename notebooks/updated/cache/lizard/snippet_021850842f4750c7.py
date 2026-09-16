def to_api_repr(self):
    configuration = self._configuration.to_api_repr()
    if self.source_uris is not None:
        _helpers._set_sub_prop(configuration, ['load', 'sourceUris'], self.
            source_uris)
    _helpers._set_sub_prop(configuration, ['load', 'destinationTable'],
        self.destination.to_api_repr())
    return {'jobReference': self._properties['jobReference'],
        'configuration': configuration}