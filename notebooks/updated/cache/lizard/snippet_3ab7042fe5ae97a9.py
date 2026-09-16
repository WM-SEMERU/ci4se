def bind(self, **bindings):
    found_vars = set()
    result = []
    for layer in self.flatten():
        if isinstance(layer, _DeferredLayer):
            var_keys = {var.key for var in six.itervalues(layer.unbound_vars)}
            layers_bindings = {k: v for k, v in six.iteritems(bindings) if 
                k in var_keys}
            result.append(layer.bind(**layers_bindings))
            found_vars.update(six.iterkeys(layers_bindings))
        else:
            result.append(layer)
    missing_vars = set(six.iterkeys(bindings)) - found_vars
    if missing_vars:
        raise ValueError('Unused bindings: %s' % missing_vars)
    return self.__class__(*result)