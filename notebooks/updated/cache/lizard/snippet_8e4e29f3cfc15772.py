def get(self, variable_path: str, default: t.Optional[t.Any]=None,
    coerce_type: t.Optional[t.Type]=None, coercer: t.Optional[t.Callable]=
    None, **kwargs):
    if self.scope:
        variable_path = '{0.scope}{0.path_separator}{1}'.format(self,
            variable_path)
    if self.key_prefix:
        variable_path = '{0.key_prefix}:{1}'.format(self, variable_path)
    val = self.client.get(variable_path)
    if val is None:
        return default
    if val.startswith(self.object_serialize_prefix):
        _val = val[len(self.object_serialize_prefix):]
        bundle = self.object_deserialize(_val)
        if bundle == '':
            return self.coerce(bundle, coerce_type=coerce_type, coercer=coercer
                )
        return bundle
    if isinstance(val, bytes):
        val = val.decode()
    return self.coerce(val, coerce_type=coerce_type, coercer=coercer)