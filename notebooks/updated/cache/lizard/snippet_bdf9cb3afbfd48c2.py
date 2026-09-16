def assign_variable_names(self):
    for var in self._variables:
        if isinstance(var, SimStackVariable):
            if var.name is not None:
                continue
            if var.ident.startswith('iarg'):
                var.name = 'arg_%x' % var.offset
            else:
                var.name = 's_%x' % -var.offset
        elif isinstance(var, SimRegisterVariable):
            if var.name is not None:
                continue
            var.name = var.ident