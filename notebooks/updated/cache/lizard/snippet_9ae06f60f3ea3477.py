def validate(self, value):
    if not isinstance(value, list):
        raise tldap.exceptions.ValidationError(
            'is not a list and max_instances is %s' % self._max_instances)
    if self._max_instances is not None and len(value) > self._max_instances:
        raise tldap.exceptions.ValidationError(
            'exceeds max_instances of %d' % self._max_instances)
    if self._required:
        if len(value) == 0:
            raise tldap.exceptions.ValidationError('is required')
    for i, v in enumerate(value):
        self.value_validate(v)