def import_from_str(value):
    try:
        parts = value.split('.')
        module_path, class_name = '.'.join(parts[:-1]), parts[-1]
        module = importlib.import_module(module_path)
        return getattr(module, class_name)
    except ImportError as e:
        msg = 'Could not import %s for settings. %s: %s.' % (value, e.
            __class__.__name__, e)
        raise ImportError(msg)