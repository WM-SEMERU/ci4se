def init_app(self, app, decorators=None):
    self.decorators = decorators or self.decorators
    self.app = app
    self.load_config(app)
    if self.template_file is not None:
        self.template = self.load_swagger_file(self.template_file)
    self.register_views(app)
    self.add_headers(app)
    if self.parse:
        if RequestParser is None:
            raise RuntimeError('Please install flask_restful')
        self.parsers = {}
        self.schemas = {}
        self.format_checker = jsonschema.FormatChecker()
        self.parse_request(app)
    self._configured = True
    app.swag = self