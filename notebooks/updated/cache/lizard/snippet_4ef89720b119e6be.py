def get_internal_modules(key='exa'):
    key += '.'
    return [v for k, v in sys.modules.items() if k.startswith(key)]