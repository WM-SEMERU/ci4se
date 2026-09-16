def find_field_meta(obj, value):
    if '__' in value:
        value_list = value.split('__')
        child_obj = obj._meta.get_field(value_list[0]).rel.to
        return find_field_meta(child_obj, '__'.join(value_list[1:]))
    return obj._meta.get_field(value)