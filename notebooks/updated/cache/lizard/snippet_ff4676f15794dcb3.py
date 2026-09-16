def check_params_types(self, method):
    mn = method.__name__
    annos = dict(method.__annotations__)
    errors = []
    msg_tuple = 'Parameter {} in method {} is not annotated with a tuple.'
    msg_ptype = 'Parameter {} in method {} is not a valid Ptype.'
    msg_mod = 'Type for param {} in method {} must descend from Model.'
    msg_cls = 'Type for param {} in method {} must be instance (not class)'
    bodies = []
    for pname, anno in annos.items():
        if pname == 'return':
            continue
        elif len(anno) != 2:
            errors.append(msg_tuple.format(pname, mn))
        else:
            param_type, value_type = anno
            if param_type not in Ptypes:
                errors.append(msg_ptype.format(pname, mn))
            elif param_type == 'body':
                bodies.append(pname)
            elif param_type == 'path':
                default = method.signature.parameters[pname].default
                if default is not inspect._empty:
                    msg = (
                        'Path prameter {} in method {} has a default value ({}) that would make it optional (which is wrong!)'
                        )
                    errors.append(msg.format(pname, mn, default))
            if hasattr(value_type, '__bases__'):
                errors.append(msg_cls.format(pname, mn))
            elif Model not in value_type.__class__.__bases__:
                errors.append(msg_mod.format(pname, mn))
    if len(bodies) > 1:
        msg = 'Too many "Ptypes.body" params {} for method {} (max=1).'
        errors.append(msg.format(bodies, mn))
    return errors