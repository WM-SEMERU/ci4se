def _validate_property_names(class_name, properties):
    for property_name in properties:
        if not property_name or property_name.startswith(
            ILLEGAL_PROPERTY_NAME_PREFIXES):
            raise IllegalSchemaStateError(
                'Class "{}" has a property with an illegal name: {}'.format
                (class_name, property_name))