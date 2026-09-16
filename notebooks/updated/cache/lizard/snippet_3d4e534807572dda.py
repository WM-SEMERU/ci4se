def find_additional_properties(instance, schema):
    properties = schema.get('properties', {})
    patterns = '|'.join(schema.get('patternProperties', {}))
    for property in instance:
        if property not in properties:
            if patterns and re.search(patterns, property):
                continue
            yield property