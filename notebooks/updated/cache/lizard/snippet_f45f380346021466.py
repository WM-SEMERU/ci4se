def _process_fields_convert_map(self, parameters, download=False):
    if 'fields_convert_map' in parameters:
        _f = parameters.get('fields_convert_map') or []
        parameters['fields_convert_map'] = self._get_fields_convert_map(_f,
            download)