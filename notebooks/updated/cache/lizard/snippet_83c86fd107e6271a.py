def from_extension(extension):
    if not extension.startswith('.'):
        raise ValueError('Extensions must begin with a period.')
    try:
        return EXTENSION_TO_TYPE[extension.lower()]
    except KeyError:
        raise UnknownExtensionError(
            'seqmagick does not know how to handle ' +
            'files with extensions like this: ' + extension)