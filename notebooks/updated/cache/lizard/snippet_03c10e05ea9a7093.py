def writeObject(self, obj):
    log_debug('Writing object of type {0}'.format(type(obj).__name__))
    if isinstance(obj, JavaArray):
        self.write_array(obj)
    elif isinstance(obj, JavaEnum):
        self.write_enum(obj)
    elif isinstance(obj, JavaObject):
        self.write_object(obj)
    elif isinstance(obj, JavaString):
        self.write_string(obj)
    elif isinstance(obj, JavaClass):
        self.write_class(obj)
    elif obj is None:
        self.write_null()
    elif type(obj) is str:
        self.write_blockdata(obj)
    else:
        raise RuntimeError('Object serialization of type {0} is not supported.'
            .format(type(obj)))