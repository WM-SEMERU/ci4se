def _to_rest_rels(model, props):
    props['to_many'] = {}
    props['to_one'] = {}
    for key in model.to_one:
        try:
            props['to_one'][key] = props.pop(key)
        except KeyError:
            continue
    for key in model.to_many:
        try:
            props['to_many'][key] = props.pop(key)
        except KeyError:
            continue