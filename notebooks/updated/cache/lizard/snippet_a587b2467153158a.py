def initialize_api(flask_app):
    if not flask_restplus:
        return
    api = flask_restplus.Api(version='1.0', title='My Example API')
    api.add_resource(HelloWorld, '/hello')
    blueprint = flask.Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    flask_app.register_blueprint(blueprint)