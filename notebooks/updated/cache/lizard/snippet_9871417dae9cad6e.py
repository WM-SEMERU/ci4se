def importSafeElementTree(module_names=None):
    if module_names is None:
        module_names = xxe_safe_elementtree_modules
    try:
        return importElementTree(module_names)
    except ImportError:
        raise ImportError(
            'Unable to find a ElementTree module that is not vulnerable to XXE. Tried importing %r'
             % (module_names,))