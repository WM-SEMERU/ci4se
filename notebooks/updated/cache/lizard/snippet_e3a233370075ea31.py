def init_app(self, app):
    self.app = app
    self.__blueprint__ = Blueprint(self.__name__, self.__name__, url_prefix
        =self.__prefix__)
    for url, name, methods in self.__urls__:
        self.blueprint.add_url_rule(url, view_func=getattr(self, name),
            endpoint=name.replace('r_', ''), methods=methods)
    self.app = self.app.register_blueprint(self.blueprint)
    return self.blueprint