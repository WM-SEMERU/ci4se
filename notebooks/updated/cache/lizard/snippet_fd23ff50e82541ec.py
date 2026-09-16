def get_index_models(index):
    models = []
    for app_model in get_index_config(index).get('models'):
        app, model = app_model.split('.')
        models.append(apps.get_model(app, model))
    return models