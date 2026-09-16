def replace_stripe_gateway_by_id(cls, stripe_gateway_id, stripe_gateway, **
    kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._replace_stripe_gateway_by_id_with_http_info(
            stripe_gateway_id, stripe_gateway, **kwargs)
    else:
        data = cls._replace_stripe_gateway_by_id_with_http_info(
            stripe_gateway_id, stripe_gateway, **kwargs)
        return data