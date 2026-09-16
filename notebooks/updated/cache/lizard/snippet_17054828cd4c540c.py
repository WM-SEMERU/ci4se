def validate_supported_property_type_id(property_name, property_type_id):
    if property_type_id not in PROPERTY_TYPE_ID_TO_NAME:
        raise AssertionError(
            'Property "{}" has unsupported property type id: {}'.format(
            property_name, property_type_id))