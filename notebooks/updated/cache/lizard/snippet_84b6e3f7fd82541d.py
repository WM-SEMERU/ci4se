def _get_widget_id(self, package_name):
    widget_id = ''
    for app in self.get_apps_list():
        if app.package == package_name:
            widget_id = list(app.widgets.keys())[0]
    return widget_id