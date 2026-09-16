def replace_option_by_id(cls, option_id, option, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._replace_option_by_id_with_http_info(option_id, option,
            **kwargs)
    else:
        data = cls._replace_option_by_id_with_http_info(option_id, option,
            **kwargs)
        return data