def get(self, name):
    logger.debug('VipsObject.get: name = %s', name)
    pspec = self._get_pspec(name)
    if pspec is None:
        raise Error('Property not found.')
    gtype = pspec.value_type
    gv = pyvips.GValue()
    gv.set_type(gtype)
    go = ffi.cast('GObject *', self.pointer)
    gobject_lib.g_object_get_property(go, _to_bytes(name), gv.pointer)
    return gv.get()