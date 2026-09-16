def init_app(self, app):
    self.init_config(app)
    if hasattr(app, 'cli'):
        app.cli.add_command(files_cmd)
    app.extensions['invenio-files-rest'] = _FilesRESTState(app)