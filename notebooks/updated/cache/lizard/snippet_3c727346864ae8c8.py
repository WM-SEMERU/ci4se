def validate(self, schema=None):
    if schema is None:
        schema = self._schema
    type_checker = Draft3Validator.TYPE_CHECKER.redefine('datetime', lambda
        c, d: isinstance(d, (datetime.date, datetime.datetime)))
    ValidatorCls = jsonschema.validators.extend(Draft3Validator,
        type_checker=type_checker)
    validator = ValidatorCls(schema, format_checker=FormatChecker())
    errors = [str(error) for error in validator.iter_errors(self.as_dict())]
    if errors:
        raise ScrapeValueError('validation of {} {} failed: {}'.format(self
            .__class__.__name__, self._id, '\n\t' + '\n\t'.join(errors)))