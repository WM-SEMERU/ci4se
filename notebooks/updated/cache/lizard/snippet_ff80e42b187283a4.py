def set_value(self, name, value, PY2_frontend):
    import cloudpickle
    ns = self._get_reference_namespace(name)
    svalue = value[0]
    if PY2_frontend and not PY2:
        svalue = bytes(svalue, 'latin-1')
    dvalue = cloudpickle.loads(svalue)
    ns[name] = dvalue
    self.log.debug(ns)