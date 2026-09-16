def ParseOptions(cls, options, configuration_object):
    if not isinstance(configuration_object, tools.CLITool):
        raise errors.BadConfigObject(
            'Configuration object is not an instance of CLITool')
    process_memory_limit = cls._ParseNumericOption(options,
        'process_memory_limit')
    if process_memory_limit and process_memory_limit < 0:
        raise errors.BadConfigOption(
            'Invalid process memory limit value cannot be negative.')
    setattr(configuration_object, '_process_memory_limit', process_memory_limit
        )