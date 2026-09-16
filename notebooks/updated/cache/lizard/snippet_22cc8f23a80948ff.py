def load(modname, verbose=False, failfast=False):
    for app in settings.INSTALLED_APPS:
        get_module(app, modname, verbose, failfast)