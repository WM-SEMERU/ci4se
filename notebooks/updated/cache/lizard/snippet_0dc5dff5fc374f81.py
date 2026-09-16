def get_library_version(module_name):
    try:
        module = importlib.import_module('luma.' + module_name)
        if hasattr(module, '__version__'):
            return module.__version__
        else:
            return None
    except ImportError:
        return None