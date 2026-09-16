def dcos_user(user_id, password):
    o_token = dcos_acs_token()
    token = shakedown.authenticate(user_id, password)
    dcos.config.set_val('core.dcos_acs_token', token)
    yield
    dcos.config.set_val('core.dcos_acs_token', o_token)