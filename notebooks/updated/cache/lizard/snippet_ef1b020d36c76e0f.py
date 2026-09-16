def delete_wish_list_by_id(cls, wish_list_id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._delete_wish_list_by_id_with_http_info(wish_list_id, **
            kwargs)
    else:
        data = cls._delete_wish_list_by_id_with_http_info(wish_list_id, **
            kwargs)
        return data