def create_model_table(self, model):
    try:
        return db_model_factory(self.Base, model, self.models)
    except Exception as exc:
        raise ModelError(model.name, message=
            'failed to create in-memory table.', orig_exc=exc, context=self
            .error_context)