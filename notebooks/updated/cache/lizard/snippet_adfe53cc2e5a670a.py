def extract_version(filepath='jeni.py', name='__version__'):
    context = {}
    for line in open(filepath):
        if name in line:
            exec(line, context)
            break
    else:
        raise RuntimeError('{} not found in {}'.format(name, filepath))
    return context[name]