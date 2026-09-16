def set_genus_type(self, genus_type=None):
    if genus_type is None:
        raise NullArgument()
    metadata = Metadata(**settings.METADATA['genus_type'])
    metadata_id = Metadata(**settings.METADATA['genus_type_id'])
    if metadata.is_read_only():
        raise NoAccess()
    if self._is_valid_input(genus_type, metadata, array=False):
        self._my_map['genusTypeId'] = str(genus_type)
    elif self._is_valid_input(genus_type, metadata_id, array=False):
        self._my_map['genusTypeId'] = str(genus_type)
    else:
        raise InvalidArgument