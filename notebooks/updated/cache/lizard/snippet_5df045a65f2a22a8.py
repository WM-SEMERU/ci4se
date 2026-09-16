def validate_yaml(self, properties):
    validator = OurValidator(schema)
    if not validator.validate(properties):
        for key, value in validator.errors.items():
            if any([('unallowed value' in v) for v in value]):
                print(
                    '{key} has an illegal value. Allowed values are {values} and are case sensitive.'
                    .format(key=key, values=schema[key]['allowed']))
        raise ValueError(validator.errors)