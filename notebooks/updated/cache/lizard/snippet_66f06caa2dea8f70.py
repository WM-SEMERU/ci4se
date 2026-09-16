def validate_many(d, schema):
    return [validator.to_python(d.get(key), state=key) for key, validator in
        schema]