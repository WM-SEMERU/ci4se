def delete_free_shipping_promotion_by_id(cls, free_shipping_promotion_id,
    **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._delete_free_shipping_promotion_by_id_with_http_info(
            free_shipping_promotion_id, **kwargs)
    else:
        data = cls._delete_free_shipping_promotion_by_id_with_http_info(
            free_shipping_promotion_id, **kwargs)
        return data