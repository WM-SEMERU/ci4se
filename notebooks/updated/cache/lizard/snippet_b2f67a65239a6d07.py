def _validate(self):
    errors = []
    for k in self._defaults.keys():
        try:
            validator = self._defaults[k]['validator']
            if validator is not None:
                self[k] = validator(self[k])
        except ValueError as e:
            errors.append('\t{}: {}'.format(k, six.text_type(e)))
    if errors:
        raise ValueError('Invalid configuration values were set: \n{}'.
            format('\n'.join(errors)))