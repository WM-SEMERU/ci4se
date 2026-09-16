def replace_free_shipping_by_id(cls, free_shipping_id, free_shipping, **kwargs
    ):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._replace_free_shipping_by_id_with_http_info(free_shipping_id
            , free_shipping, **kwargs)
    else:
        data = cls._replace_free_shipping_by_id_with_http_info(free_shipping_id
            , free_shipping, **kwargs)
        return data