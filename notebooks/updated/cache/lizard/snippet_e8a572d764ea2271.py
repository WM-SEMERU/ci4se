def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(CONFIG[config_name])
    BOOTSTRAP.init_app(app)
    from flask_seguro.controllers.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app