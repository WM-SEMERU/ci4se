def create_braintree_gateway(cls, braintree_gateway, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._create_braintree_gateway_with_http_info(braintree_gateway,
            **kwargs)
    else:
        data = cls._create_braintree_gateway_with_http_info(braintree_gateway,
            **kwargs)
        return data