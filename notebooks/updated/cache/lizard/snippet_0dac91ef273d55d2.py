def get_product_by_id(cls, product_id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._get_product_by_id_with_http_info(product_id, **kwargs)
    else:
        data = cls._get_product_by_id_with_http_info(product_id, **kwargs)
        return data