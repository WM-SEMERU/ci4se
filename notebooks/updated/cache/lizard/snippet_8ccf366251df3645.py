def ParseOptions(cls, options, configuration_object):
    if not isinstance(configuration_object, tools.CLITool):
        raise errors.BadConfigObject(
            'Configuration object is not an instance of CLITool')
    storage_format = cls._ParseStringOption(options, 'storage_format')
    if not storage_format:
        raise errors.BadConfigOption('Unable to determine storage format.')
    if storage_format not in definitions.STORAGE_FORMATS:
        raise errors.BadConfigOption('Unsupported storage format: {0:s}'.
            format(storage_format))
    setattr(configuration_object, '_storage_format', storage_format)