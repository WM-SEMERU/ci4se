def _is_not_pickle_safe_gl_model_class(obj_class):
    if issubclass(obj_class, _toolkits._model.CustomModel):
        return not obj_class._is_gl_pickle_safe()
    return False