def is_builtin_css_function(name):
    name = name.replace('_', '-')
    if name in BUILTIN_FUNCTIONS:
        return True
    if name[0] == '-' and '-' in name[1:]:
        return True
    return False