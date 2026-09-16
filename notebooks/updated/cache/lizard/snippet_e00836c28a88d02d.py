def supported_types_for_non_geo_entity(country_code):
    metadata = PhoneMetadata.metadata_for_nongeo_region(country_code, None)
    if metadata is None:
        return set()
    return _supported_types_for_metadata(metadata)