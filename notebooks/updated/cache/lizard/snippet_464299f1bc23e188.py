def delete_store_credit_by_id(cls, store_credit_id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._delete_store_credit_by_id_with_http_info(store_credit_id,
            **kwargs)
    else:
        data = cls._delete_store_credit_by_id_with_http_info(store_credit_id,
            **kwargs)
        return data