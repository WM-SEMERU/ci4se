def validate(self):
    validator = Draft7Validator(self.SCHEMA)
    errors = set()
    for error in validator.iter_errors(self.serialize()):
        errors.add('.'.join(list(map(str, error.path)) + [error.message]))
    if errors:
        raise JSONValidationException(type(self).__name__, errors)