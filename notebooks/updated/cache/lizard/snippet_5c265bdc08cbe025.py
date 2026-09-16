def show_state_usage(queue=False, **kwargs):
    conflict = _check_queue(queue, kwargs)
    if conflict is not None:
        return conflict
    pillar = kwargs.get('pillar')
    pillar_enc = kwargs.get('pillar_enc')
    if pillar_enc is None and pillar is not None and not isinstance(pillar,
        dict):
        raise SaltInvocationError(
            'Pillar data must be formatted as a dictionary, unless pillar_enc is specified.'
            )
    st_ = salt.state.HighState(__opts__, pillar, pillar_enc=pillar_enc)
    st_.push_active()
    try:
        ret = st_.compile_state_usage()
    finally:
        st_.pop_active()
    _set_retcode(ret)
    return ret