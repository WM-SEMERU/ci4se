def is_valid(hal_id):
    match = REGEX.match(hal_id)
    return match is not None and match.group(0) == hal_id