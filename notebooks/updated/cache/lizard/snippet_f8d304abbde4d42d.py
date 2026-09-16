def clean_cache():
    import importlib
    try:
        vermod = importlib.import_module('versioneer')
        globals()['versioneer'] = vermod
    except ImportError:
        importlib.invalidate_caches()