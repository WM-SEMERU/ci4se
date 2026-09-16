def _validate_resource_dict(cls, logical_id, resource_dict):
    if 'Type' not in resource_dict:
        raise InvalidResourceException(logical_id,
            "Resource dict missing key 'Type'.")
    if resource_dict['Type'] != cls.resource_type:
        raise InvalidResourceException(logical_id,
            "Resource has incorrect Type; expected '{expected}', got '{actual}'"
            .format(expected=cls.resource_type, actual=resource_dict['Type']))
    if 'Properties' in resource_dict and not isinstance(resource_dict[
        'Properties'], dict):
        raise InvalidResourceException(logical_id,
            'Properties of a resource must be an object.')