def import_json():
    global _json_module
    if _json_module is not None:
        return _json_module
    else:
        try:
            module = __import__('json')
        except ImportError:
            raise ImportError('Could not import the json module')
        else:
            _json_module = module
            return module