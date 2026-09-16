def delete_zip_codes_geo_zone_by_id(cls, zip_codes_geo_zone_id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._delete_zip_codes_geo_zone_by_id_with_http_info(
            zip_codes_geo_zone_id, **kwargs)
    else:
        data = cls._delete_zip_codes_geo_zone_by_id_with_http_info(
            zip_codes_geo_zone_id, **kwargs)
        return data