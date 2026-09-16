def load_model_from_path(model_path, meta=False, **overrides):
    if not meta:
        meta = get_model_meta(model_path)
    cls = get_lang_class(meta['lang'])
    nlp = cls(meta=meta, **overrides)
    pipeline = meta.get('pipeline', [])
    disable = overrides.get('disable', [])
    if pipeline is True:
        pipeline = nlp.Defaults.pipe_names
    elif pipeline in (False, None):
        pipeline = []
    for name in pipeline:
        if name not in disable:
            config = meta.get('pipeline_args', {}).get(name, {})
            component = nlp.create_pipe(name, config=config)
            nlp.add_pipe(component, name=name)
    return nlp.from_disk(model_path)