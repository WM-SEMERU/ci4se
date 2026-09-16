def update_payment_token_by_id(cls, payment_token_id, payment_token, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._update_payment_token_by_id_with_http_info(payment_token_id,
            payment_token, **kwargs)
    else:
        data = cls._update_payment_token_by_id_with_http_info(payment_token_id,
            payment_token, **kwargs)
        return data