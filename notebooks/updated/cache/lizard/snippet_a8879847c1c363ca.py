def _init_module_cache():
    if len(FieldTranslation._modules) < len(FieldTranslation.
        _model_module_paths):
        for module_path in FieldTranslation._model_module_paths:
            FieldTranslation._modules[module_path] = importlib.import_module(
                module_path)
        return True
    return False