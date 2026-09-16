def _split_mod_var_names(resource_name):
    try:
        dot_index = resource_name.rindex('.')
    except ValueError:
        return '', resource_name
    return resource_name[:dot_index], resource_name[dot_index + 1:]