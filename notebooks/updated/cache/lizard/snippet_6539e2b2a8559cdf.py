def CheckFile(self, path):
    print('Checking: {0:s}'.format(path))
    definitions_registry = registry.DataTypeDefinitionsRegistry()
    definitions_reader = reader.YAMLDataTypeDefinitionsFileReader()
    result = False
    try:
        definitions_reader.ReadFile(definitions_registry, path)
        result = True
    except KeyError as exception:
        logging.warning(
            'Unable to register data type definition in file: {0:s} with error: {1:s}'
            .format(path, exception))
    except errors.FormatError as exception:
        logging.warning('Unable to validate file: {0:s} with error: {1:s}'.
            format(path, exception))
    return result