def get_cash_on_delivery_payment_by_id(cls, cash_on_delivery_payment_id, **
    kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._get_cash_on_delivery_payment_by_id_with_http_info(
            cash_on_delivery_payment_id, **kwargs)
    else:
        data = cls._get_cash_on_delivery_payment_by_id_with_http_info(
            cash_on_delivery_payment_id, **kwargs)
        return data