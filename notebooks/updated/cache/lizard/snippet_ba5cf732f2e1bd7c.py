def retro_schema(schema):
    output = wrap({'mappings': {typename: {'dynamic_templates': [
        retro_dynamic_template(*t.items()[0]) for t in details.
        dynamic_templates], 'properties': retro_properties(details.
        properties)} for typename, details in schema.mappings.items()},
        'settings': schema.settings})
    return output