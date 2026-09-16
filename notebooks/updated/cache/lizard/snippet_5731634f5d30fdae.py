def replace_customer_group_by_id(cls, customer_group_id, customer_group, **
    kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._replace_customer_group_by_id_with_http_info(
            customer_group_id, customer_group, **kwargs)
    else:
        data = cls._replace_customer_group_by_id_with_http_info(
            customer_group_id, customer_group, **kwargs)
        return data