def ensure_nest_alts_are_valid_alts(nest_spec, list_elements, all_ids):
    invalid_alt_ids = []
    for x in list_elements:
        if x not in all_ids:
            invalid_alt_ids.append(x)
    if invalid_alt_ids != []:
        msg = 'The following elements are not in df[alt_id_col]: {}'
        raise ValueError(msg.format(invalid_alt_ids))
    return None