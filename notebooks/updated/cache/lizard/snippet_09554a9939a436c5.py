def CreateClass(cls, data_type_definition):
    cls._ValidateDataTypeDefinition(data_type_definition)
    class_definition = cls._CreateClassTemplate(data_type_definition)
    namespace = {'__builtins__': {'object': builtins.object, 'super':
        builtins.super}, '__name__': '{0:s}'.format(data_type_definition.name)}
    if sys.version_info[0] >= 3:
        namespace['__builtins__']['__build_class__'] = builtins.__build_class__
    exec(class_definition, namespace)
    return namespace[data_type_definition.name]