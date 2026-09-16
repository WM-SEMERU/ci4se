def replace_refund_transaction_by_id(cls, refund_transaction_id,
    refund_transaction, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._replace_refund_transaction_by_id_with_http_info(
            refund_transaction_id, refund_transaction, **kwargs)
    else:
        data = cls._replace_refund_transaction_by_id_with_http_info(
            refund_transaction_id, refund_transaction, **kwargs)
        return data