def uuid(uuid_value=None):
    if uuid_value:
        if not validate_uuid(uuid_value):
            raise ValueError('uuid_value must be a valid UUID version 4 object'
                )
    else:
        uuid_value = uuid.uuid4()
    if versions_settings.VERSIONS_USE_UUIDFIELD:
        return uuid_value
    else:
        return six.u(str(uuid_value))