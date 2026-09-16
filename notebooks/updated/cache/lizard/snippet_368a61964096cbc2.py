def SetProperties(has_props_cls, input_dict, include_immutable=True):
    props = has_props_cls()
    if not isinstance(input_dict, (dict, collections.OrderedDict)):
        raise RuntimeError('input_dict invalid: ', input_dict)
    for k, v in iter(input_dict.items()):
        if k in has_props_cls._props and (include_immutable or any(hasattr(
            has_props_cls._props[k], att) for att in ('required', 'new_name'))
            ):
            p = props._props.get(k)
            if isinstance(p, properties.HasProperties):
                props._set(k, SetProperties(p, v, include_immutable=
                    include_immutable))
            elif isinstance(p, properties.Instance):
                props._set(k, SetProperties(p.instance_class, v,
                    include_immutable=include_immutable))
            elif isinstance(p, properties.List):
                if not isinstance(v, list):
                    raise RuntimeError('property value mismatch', p, v)
                if not isinstance(v[0], properties.HasProperties):
                    prop = p.prop.instance_class
                    newlist = []
                    for i in v:
                        value = SetProperties(prop, i, include_immutable=
                            include_immutable)
                        newlist.append(value)
                    props._set(k, newlist)
                else:
                    props._set(k, v)
            else:
                props._set(k, p.from_json(v))
    return props