def checkout(cls, order, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._checkout_with_http_info(order, **kwargs)
    else:
        data = cls._checkout_with_http_info(order, **kwargs)
        return data