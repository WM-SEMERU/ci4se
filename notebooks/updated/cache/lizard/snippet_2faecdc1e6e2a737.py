def is_sms_service_for_region(numobj, region_dialing_from):
    if not _region_dialing_from_matches_number(numobj, region_dialing_from):
        return False
    metadata = PhoneMetadata.short_metadata_for_region(region_dialing_from)
    return (metadata is not None and
        _matches_possible_number_and_national_number(
        national_significant_number(numobj), metadata.sms_services))