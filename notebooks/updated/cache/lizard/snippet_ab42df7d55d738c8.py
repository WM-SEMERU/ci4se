def get_name(cls):
    global _registry_loaded
    if not _registry_loaded:
        load_message_classes()
    try:
        return _class_to_schema_name[cls]
    except KeyError:
        raise TypeError(
            'The class {} is not in the message registry, which indicates it is not in the current list of entry points for "fedora_messaging". Please check that the class has been added to your package\'s entry points.'
            .format(repr(cls)))