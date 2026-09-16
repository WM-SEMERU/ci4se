def _normalize_input_factory(alg):
    normalization_form = 'NFKD' if alg & ns.COMPATIBILITYNORMALIZE else 'NFD'
    wrapped = partial(normalize, normalization_form)
    if NEWPY:
        return wrapped
    else:
        return lambda x, _f=wrapped: _f(x) if isinstance(x, py23_str) else x