def remove(self, spec_or_id=None, multi=True, **kwargs):
    warnings.warn(
        'remove is deprecated. Use delete_one or delete_many instead.',
        DeprecationWarning, stacklevel=2)
    if spec_or_id is None:
        spec_or_id = {}
    if not isinstance(spec_or_id, collections.Mapping):
        spec_or_id = {'_id': spec_or_id}
    write_concern = None
    collation = validate_collation_or_none(kwargs.pop('collation', None))
    if kwargs:
        write_concern = WriteConcern(**kwargs)
    with self._socket_for_writes() as sock_info:
        return self._delete(sock_info, spec_or_id, multi, write_concern,
            collation=collation)