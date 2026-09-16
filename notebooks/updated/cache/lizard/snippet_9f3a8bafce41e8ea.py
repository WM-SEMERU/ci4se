def get_template_sources(self, template_name):
    if ':' not in template_name:
        self.reset(True)
        return
    app, template_path = template_name.split(':')
    if app:
        yield NamespaceOrigin(app_name=app, name='app_namespace:%s:%s' % (
            app, template_name), template_name=template_path, loader=self)
        return
    self.reset(False)
    for app in self.app_templates_dirs:
        file_path = self.get_app_template_path(app, template_path)
        if file_path in self._already_used:
            continue
        self._already_used.append(file_path)
        yield NamespaceOrigin(app_name=app, name='app_namespace:%s:%s' % (
            app, template_name), template_name=template_path, loader=self)