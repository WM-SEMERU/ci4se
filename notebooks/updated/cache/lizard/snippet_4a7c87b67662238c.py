def loadUi(uifile, baseinstance=None, package='', resource_suffix='_rc'):
    from .Loader.loader import DynamicUILoader
    return DynamicUILoader(package).loadUi(uifile, baseinstance,
        resource_suffix)