def create_payment_token(cls, payment_token, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._create_payment_token_with_http_info(payment_token, **kwargs
            )
    else:
        data = cls._create_payment_token_with_http_info(payment_token, **kwargs
            )
        return data