def get_apps(self):
    templates = []
    for app in settings.INSTALLED_APPS:
        try:
            app = import_module(app + '.emails')
            templates += self.get_plugs_mail_classes(app)
        except ImportError:
            pass
    return templates