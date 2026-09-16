def load_model(model_cls_path, model_cls_name, model_load_args):
    spec = importlib.util.spec_from_file_location('active_model',
        model_cls_path)
    model_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(model_module)
    model_cls = getattr(model_module, model_cls_name)
    model = model_cls()
    if not isinstance(model, BaseModel):
        warnings.warn("Loaded model '%s' at '%s' is not an instance of %r" %
            (model_cls_name, model_cls_path, BaseModel))
    model.load(**model_load_args)
    return model