def setup_authentication_methods(authn_config, template_env):
    routing = {}
    ac = AuthnBroker()
    for authn_method in authn_config:
        cls = make_cls_from_name(authn_method['class'])
        instance = cls(template_env=template_env, **authn_method['kwargs'])
        ac.add(authn_method['acr'], instance)
        routing[instance.url_endpoint] = VerifierMiddleware(instance)
    return ac, routing