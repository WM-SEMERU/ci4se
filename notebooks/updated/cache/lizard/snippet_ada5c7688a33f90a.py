def value_to_jam(value, methods=False):
    global __value_id
    r = __python_to_jam.get(value, None)
    if r:
        return r
    exported_name = '###_' + str(__value_id)
    __value_id = __value_id + 1
    __python_to_jam[value] = exported_name
    __jam_to_python[exported_name] = value
    if methods and type(value) == types.InstanceType:
        for field_name in dir(value):
            field = getattr(value, field_name)
            if callable(field) and not field_name.startswith('__'):
                bjam.import_rule('', exported_name + '.' + field_name, field)
    return exported_name