def delete_payment_token_by_id(cls, payment_token_id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._delete_payment_token_by_id_with_http_info(payment_token_id,
            **kwargs)
    else:
        data = cls._delete_payment_token_by_id_with_http_info(payment_token_id,
            **kwargs)
        return data