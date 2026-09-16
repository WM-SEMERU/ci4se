def replace_address_by_id(cls, address_id, address, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._replace_address_by_id_with_http_info(address_id,
            address, **kwargs)
    else:
        data = cls._replace_address_by_id_with_http_info(address_id,
            address, **kwargs)
        return data