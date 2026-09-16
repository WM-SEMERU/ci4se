def delete_order_by_id(cls, order_id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._delete_order_by_id_with_http_info(order_id, **kwargs)
    else:
        data = cls._delete_order_by_id_with_http_info(order_id, **kwargs)
        return data