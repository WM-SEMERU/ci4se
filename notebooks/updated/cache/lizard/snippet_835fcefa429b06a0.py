def generate_random_schema(valid):
    schema_type = choice(['literal', 'type'])
    if schema_type == 'literal':
        type, gen = generate_random_type(valid)
        value = next(gen)
        return value, (value if valid else None for i in itertools.count())
    elif schema_type == 'type':
        return generate_random_type(valid)
    else:
        raise AssertionError('!')