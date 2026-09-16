def validate_enabled(enabled):
    if isinstance(enabled, six.string_types):
        if enabled.lower() not in ['on', 'off', 'yes', 'no']:
            msg = (
                """
Mac Power: Invalid String Value for Enabled.
String values must be 'on' or 'off'/'yes' or 'no'.
Passed: {0}"""
                .format(enabled))
            raise SaltInvocationError(msg)
        return 'on' if enabled.lower() in ['on', 'yes'] else 'off'
    return 'on' if bool(enabled) else 'off'