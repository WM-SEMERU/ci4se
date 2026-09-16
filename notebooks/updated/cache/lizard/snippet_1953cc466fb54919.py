def update_item(cls, item_id, item, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._update_item_with_http_info(item_id, item, **kwargs)
    else:
        data = cls._update_item_with_http_info(item_id, item, **kwargs)
        return data