def sanitize_fig_name(name):
    name, extension = os.path.splitext(name)
    return '{' + name + '}' + extension