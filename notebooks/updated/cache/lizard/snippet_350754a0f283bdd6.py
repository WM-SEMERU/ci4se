def get_module_all(node):
    all_ = None
    if '__all__' in node.locals:
        assigned = next(node.igetattr('__all__'))
        if assigned is not astroid.Uninferable:
            all_ = []
            for elt in getattr(assigned, 'elts', ()):
                try:
                    elt_name = next(elt.infer())
                except astroid.InferenceError:
                    continue
                if elt_name is astroid.Uninferable:
                    continue
                if isinstance(elt_name, astroid.Const) and isinstance(elt_name
                    .value, _STRING_TYPES):
                    all_.append(elt_name.value)
    return all_