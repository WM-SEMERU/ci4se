def serialize_to_nested(self, name, datas):
    keys = datas.get('keys', None)
    splitter = datas.get('splitter', self._DEFAULT_SPLITTER)
    if not keys:
        msg = (
            "Nested reference '{}' lacks of required 'keys' variable or is empty"
            )
        raise SerializerError(msg.format(name))
    else:
        keys = self.value_splitter(name, 'keys', keys, mode=splitter)
    context = OrderedDict()
    for k in keys:
        context[k] = OrderedDict()
    for k, v in datas.items():
        if k not in ('keys', 'structure', 'splitter'):
            values = self.value_splitter(name, 'values', v, mode=splitter)
            if len(values) != len(keys):
                msg = (
                    "Nested reference '{}' has different length for values of '{}' and 'keys'"
                    )
                raise SerializerError(msg.format(name, k))
            for i, item in enumerate(values):
                ref = keys[i]
                context[ref][k] = item
    return context