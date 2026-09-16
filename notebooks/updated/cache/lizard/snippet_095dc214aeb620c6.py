def create_uni_method(op_name, klass, jacobians=None):
    op_modules = [operator, builtins]
    op_names = [op_name, op_name + '_']
    op_function_base = find_element(op_names, op_modules, error_on_fail=True)

    def op_function(self):
        return op_function_base(self)

    def new_method(self):
        if not check_special_methods():
            raise NotImplementedError(
                'Special method %s called on %s, but special methods have been disabled. Set pymc.special_methods_available to True to enable them.'
                 % (op_name, str(self)))
        jacobian_formats = {'self': 'transformation_operation'}
        return pm.Deterministic(op_function, 
            'A Deterministic returning the value of %s(%s)' % (op_name,
            self.__name__), '(' + op_name + '_' + self.__name__ + ')',
            parents={'self': self}, trace=False, plot=False, jacobians=
            jacobians, jacobian_formats=jacobian_formats)
    new_method.__name__ = '__' + op_name + '__'
    setattr(klass, new_method.__name__, UnboundMethodType(new_method, None,
        klass))