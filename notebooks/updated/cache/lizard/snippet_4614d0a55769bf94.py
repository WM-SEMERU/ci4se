def _get_log_model_class(self):
    if self.log_model_class is not None:
        return self.log_model_class
    app_label, model_label = self.log_model.rsplit('.', 1)
    self.log_model_class = apps.get_model(app_label, model_label)
    return self.log_model_class