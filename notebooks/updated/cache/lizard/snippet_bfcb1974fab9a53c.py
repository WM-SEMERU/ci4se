def format_obj_name(obj, delim='<>'):
    pname = ''
    parent_name = get_parent_name(obj)
    if parent_name:
        pname = '{}{}{}'.format(delim[0], get_parent_name(obj), delim[1])
    return '{}{}'.format(get_obj_name(obj), pname)