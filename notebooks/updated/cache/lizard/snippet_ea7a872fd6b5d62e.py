def _supported_types_for_metadata(metadata):
    numtypes = set()
    for numtype in PhoneNumberType.values():
        if numtype in (PhoneNumberType.FIXED_LINE_OR_MOBILE,
            PhoneNumberType.UNKNOWN):
            continue
        if _desc_has_data(_number_desc_by_type(metadata, numtype)):
            numtypes.add(numtype)
    return numtypes