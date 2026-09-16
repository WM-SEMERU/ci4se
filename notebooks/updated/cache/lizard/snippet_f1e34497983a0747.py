def fix_var_name(var_name):
    name = var_name.strip()
    for char in '(). /#,':
        name = name.replace(char, '_')
    name = name.replace('+', 'pos_')
    name = name.replace('-', 'neg_')
    if name.endswith('_'):
        name = name[:-1]
    return name