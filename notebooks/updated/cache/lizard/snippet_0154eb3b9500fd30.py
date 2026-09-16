def get_spam_checker(backend_path):
    try:
        backend_module = import_module(backend_path)
        backend = getattr(backend_module, 'backend')
    except (ImportError, AttributeError):
        warnings.warn('%s backend cannot be imported' % backend_path,
            RuntimeWarning)
        backend = None
    except ImproperlyConfigured as e:
        warnings.warn(str(e), RuntimeWarning)
        backend = None
    return backend