def import_event_modules():
    for installed_app in getsetting('INSTALLED_APPS'):
        module_name = '{}.{}'.format(installed_app, EVENTS_MODULE_NAME)
        try:
            import_module(module_name)
        except ImportError:
            pass