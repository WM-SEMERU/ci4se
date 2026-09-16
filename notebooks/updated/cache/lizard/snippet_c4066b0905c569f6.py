def _validate_min_version(min_version):
    if min_version is not None:
        try:
            parsed_min_version = version.StrictVersion(min_version)
        except ValueError:
            return ExtensionVersionResult(error_reason=
                ExtensionValidationError.UNPARSEABLE_REQUESTED_VERSION,
                requested_extension_version=min_version)
        if parsed_min_version > HANDLER_VERSION:
            return ExtensionVersionResult(error_reason=
                ExtensionValidationError.OUTDATED_VERSION,
                requested_extension_version=str(parsed_min_version))
    return ExtensionVersionResult(error_reason=None,
        requested_extension_version=min_version)