def send_post(self, mri, method_name, **params):
    typ, parameters = convert_to_type_tuple_value(serialize_object(params))
    uri = NTURI(typ[2])
    uri = uri.wrap(path='%s.%s' % (mri, method_name), kws=parameters,
        scheme='pva')
    value = self._ctxt.rpc(mri, uri, timeout=None)
    return convert_value_to_dict(value)