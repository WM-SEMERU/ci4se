def tuple_sealer(fields, defaults):
    baseclass_name = 'FieldsBase_for__{0}'.format('__'.join(fields))
    global_namespace, local_namespace = make_init_func(fields, defaults,
        baseclass_name, header_name='__new__', header_start=
        'def {func_name}(cls', header_end='):\n', super_call_start=
        'return tuple.__new__(cls, (', super_call_end='))\n',
        super_call_pass_kwargs=False, set_attributes=False)

    def __getnewargs__(self):
        return tuple(self)

    def __repr__(self):
        return '{0}({1})'.format(self.__class__.__name__, ', '.join(a + '=' +
            repr(getattr(self, a)) for a in fields))
    return type(baseclass_name, (tuple,), dict([(name, property(itemgetter(
        i))) for i, name in enumerate(fields)], __new__=local_namespace[
        '__new__'], __getnewargs__=__getnewargs__, __repr__=__repr__,
        __slots__=()))