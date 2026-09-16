def get_states_geo_zone_by_id(cls, states_geo_zone_id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._get_states_geo_zone_by_id_with_http_info(states_geo_zone_id
            , **kwargs)
    else:
        data = cls._get_states_geo_zone_by_id_with_http_info(states_geo_zone_id
            , **kwargs)
        return data