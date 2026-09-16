def replace_country_by_id(cls, country_id, country, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._replace_country_by_id_with_http_info(country_id,
            country, **kwargs)
    else:
        data = cls._replace_country_by_id_with_http_info(country_id,
            country, **kwargs)
        return data