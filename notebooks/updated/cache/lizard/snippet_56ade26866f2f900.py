def create_table_rate_shipping(cls, table_rate_shipping, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._create_table_rate_shipping_with_http_info(
            table_rate_shipping, **kwargs)
    else:
        data = cls._create_table_rate_shipping_with_http_info(
            table_rate_shipping, **kwargs)
        return data