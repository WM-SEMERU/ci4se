def delete_discount_promotion_by_id(cls, discount_promotion_id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._delete_discount_promotion_by_id_with_http_info(
            discount_promotion_id, **kwargs)
    else:
        data = cls._delete_discount_promotion_by_id_with_http_info(
            discount_promotion_id, **kwargs)
        return data