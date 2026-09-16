def create_countries_geo_zone(cls, countries_geo_zone, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._create_countries_geo_zone_with_http_info(countries_geo_zone
            , **kwargs)
    else:
        data = cls._create_countries_geo_zone_with_http_info(countries_geo_zone
            , **kwargs)
        return data