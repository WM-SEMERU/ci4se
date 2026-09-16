def parse_subcomponent(text, name=None, datatype='ST', version=None,
    validation_level=None):
    version = _get_version(version)
    validation_level = _get_validation_level(validation_level)
    return SubComponent(name=name, datatype=datatype, value=text, version=
        version, validation_level=validation_level)