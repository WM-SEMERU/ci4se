def supports_object_type(self, object_type=None):
    from .osid_errors import IllegalState, NullArgument
    if not object_type:
        raise NullArgument('no input Type provided')
    if self._kwargs['syntax'] not in ['``OBJECT``']:
        raise IllegalState('put more meaninful message here')
    return object_type in self.get_object_types