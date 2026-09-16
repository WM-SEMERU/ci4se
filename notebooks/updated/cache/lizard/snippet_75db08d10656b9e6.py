def list_all_products(cls, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._list_all_products_with_http_info(**kwargs)
    else:
        data = cls._list_all_products_with_http_info(**kwargs)
        return data