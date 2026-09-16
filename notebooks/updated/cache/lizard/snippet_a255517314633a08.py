def out_filename(template, n_val, mode):
    return '{0}_{1}_{2}.cpp'.format(template.name, n_val, mode.identifier)