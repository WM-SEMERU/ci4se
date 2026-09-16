def _set_seo_models(self, value):
    seo_models = []
    for model_name in value:
        if '.' in model_name:
            app_label, model_name = model_name.split('.', 1)
            model = apps.get_model(app_label, model_name)
            if model:
                seo_models.append(model)
        else:
            app = apps.get_app_config(model_name)
            if app:
                seo_models.extend(app.get_models())
    self.seo_models = seo_models