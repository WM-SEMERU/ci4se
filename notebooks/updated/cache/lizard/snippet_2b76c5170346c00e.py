def build_getter(validator, getter_namespace=None):

    def proxy_register(key_name, default=UndefToken, help=None, namespace=None
        ):
        name = namespace or getter_namespace or config.DEFAULT
        namespace = config.get_namespace(name)
        return proxy_factory.build(validator, namespace, key_name, default,
            help)
    return proxy_register