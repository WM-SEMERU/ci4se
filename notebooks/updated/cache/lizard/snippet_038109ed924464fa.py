def experiment_property(prop):
    exp = experiment(session)
    p = getattr(exp, prop)
    return success_response(field=prop, data=p, request_type=prop)