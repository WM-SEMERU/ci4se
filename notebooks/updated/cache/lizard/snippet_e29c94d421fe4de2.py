def create_casting_method(op, klass):

    def new_method(self, op=op):
        if not check_special_methods():
            raise NotImplementedError(
                'Special method %s called on %s, but special methods have been disabled. Set pymc.special_methods_available to True to enable them.'
                 % (op_name, str(self)))
        return op(self.value)
    new_method.__name__ = '__' + op.__name__ + '__'
    setattr(klass, new_method.__name__, UnboundMethodType(new_method, None,
        klass))