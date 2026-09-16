def readObject(self):
    ref = self.readInteger(False)
    if ref & REFERENCE_BIT == 0:
        obj = self.context.getObject(ref >> 1)
        if obj is None:
            raise pyamf.ReferenceError('Unknown reference %d' % (ref >> 1,))
        if self.use_proxies is True:
            obj = self.readProxy(obj)
        return obj
    ref >>= 1
    class_def = self._getClassDefinition(ref)
    alias = class_def.alias
    obj = alias.createInstance(codec=self)
    obj_attrs = dict()
    self.context.addObject(obj)
    if class_def.encoding in (ObjectEncoding.EXTERNAL, ObjectEncoding.PROXY):
        obj.__readamf__(DataInput(self))
        if self.use_proxies is True:
            obj = self.readProxy(obj)
        return obj
    elif class_def.encoding == ObjectEncoding.DYNAMIC:
        self._readStatic(class_def, obj_attrs)
        self._readDynamic(class_def, obj_attrs)
    elif class_def.encoding == ObjectEncoding.STATIC:
        self._readStatic(class_def, obj_attrs)
    else:
        raise pyamf.DecodeError('Unknown object encoding')
    alias.applyAttributes(obj, obj_attrs, codec=self)
    if self.use_proxies is True:
        obj = self.readProxy(obj)
    return obj