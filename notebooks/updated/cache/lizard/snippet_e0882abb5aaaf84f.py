def __dump_validators(self):
    if hasattr(self, '_validators'):
        validators_json = []
        for validator in self._validators:
            if isinstance(validator, PropertyValidator):
                validators_json.append(validator.as_json())
            else:
                raise APIError("validator is not a PropertyValidator: '{}'"
                    .format(validator))
        if self._options.get('validators', list()) == validators_json:
            pass
        else:
            new_options = self._options.copy()
            new_options.update({'validators': validators_json})
            validate(new_options, options_json_schema)
            self._options = new_options