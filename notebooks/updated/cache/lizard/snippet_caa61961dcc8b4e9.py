def get_store_credit_transaction_by_id(cls, store_credit_transaction_id, **
    kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._get_store_credit_transaction_by_id_with_http_info(
            store_credit_transaction_id, **kwargs)
    else:
        data = cls._get_store_credit_transaction_by_id_with_http_info(
            store_credit_transaction_id, **kwargs)
        return data