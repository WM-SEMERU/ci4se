def switch_db(name):
    with app.app_context():
        app.extensions['pymongo'][mongo.config_prefix] = mongo.cx, mongo.cx[
            name]