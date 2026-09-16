def set_sdk_enabled(cls, value):
    if cls.XRAY_ENABLED_KEY in os.environ:
        cls.__SDK_ENABLED = str(os.getenv(cls.XRAY_ENABLED_KEY, 'true')).lower(
            ) != 'false'
    elif type(value) == bool:
        cls.__SDK_ENABLED = value
    else:
        cls.__SDK_ENABLED = True
        log.warning(
            'Invalid parameter type passed into set_sdk_enabled(). Defaulting to True...'
            )