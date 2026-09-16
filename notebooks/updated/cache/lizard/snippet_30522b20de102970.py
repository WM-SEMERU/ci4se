def supports_currency_type(self, currency_type=None):
    from .osid_errors import IllegalState, NullArgument
    if not currency_type:
        raise NullArgument('no input Type provided')
    if self._kwargs['syntax'] not in ['``CURRENCY``']:
        raise IllegalState('put more meaninful message here')
    return currency_type in self.get_currency_types