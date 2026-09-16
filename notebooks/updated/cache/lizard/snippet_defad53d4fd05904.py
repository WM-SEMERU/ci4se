def _ReadSupportedOS(self, definition_values, definition_object, name):
    supported_os = definition_values.get('supported_os', [])
    if not isinstance(supported_os, list):
        raise errors.FormatError('Invalid supported_os type: {0!s}'.format(
            type(supported_os)))
    undefined_supported_os = set(supported_os).difference(self.supported_os)
    if undefined_supported_os:
        error_string = (
            'Artifact definition: {0:s} undefined supported operating system: {1:s}.'
            .format(name, ', '.join(undefined_supported_os)))
        raise errors.FormatError(error_string)
    definition_object.supported_os = supported_os