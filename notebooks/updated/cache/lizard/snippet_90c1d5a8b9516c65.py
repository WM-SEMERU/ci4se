def _ParseSignatureIdentifiers(self, data_location, signature_identifiers):
    if not signature_identifiers:
        return
    if not data_location:
        raise ValueError('Missing data location.')
    path = os.path.join(data_location, 'signatures.conf')
    if not os.path.exists(path):
        raise IOError('No such format specification file: {0:s}'.format(path))
    try:
        specification_store = self._ReadSpecificationFile(path)
    except IOError as exception:
        raise IOError(
            'Unable to read format specification file: {0:s} with error: {1!s}'
            .format(path, exception))
    signature_identifiers = signature_identifiers.lower()
    signature_identifiers = [identifier.strip() for identifier in
        signature_identifiers.split(',')]
    file_entry_filter = file_entry_filters.SignaturesFileEntryFilter(
        specification_store, signature_identifiers)
    self._filter_collection.AddFilter(file_entry_filter)