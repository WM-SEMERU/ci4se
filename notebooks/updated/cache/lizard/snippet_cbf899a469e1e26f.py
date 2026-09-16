def _get_pos_name(pos_code, names='parent', english=True, pos_map=POS_MAP):
    pos_code = pos_code.lower()
    if names not in ('parent', 'child', 'all'):
        raise ValueError(
            "names must be one of 'parent', 'child', or 'all'; not '{}'".
            format(names))
    logger.debug("Getting {} POS name for '{}' formatted as '{}'.".format(
        'English' if english else 'Chinese', pos_code, names))
    for i in range(1, len(pos_code) + 1):
        try:
            pos_key = pos_code[0:i]
            pos_entry = pos_map[pos_key]
            break
        except KeyError:
            if i == len(pos_code):
                logger.warning("part of speech not recognized: '{}'".format
                    (pos_code))
                return None
    pos = pos_entry[1 if english else 0],
    if names == 'parent':
        logger.debug("Part of speech name found: '{}'".format(pos[0]))
        return pos[0]
    if len(pos_entry) == 3 and pos_key != pos_code:
        sub_map = pos_entry[2]
        logger.debug(
            "Found parent part of speech name '{}'. Descending to look for child name for '{}'"
            .format(pos_entry[1], pos_code))
        sub_pos = _get_pos_name(pos_code, names, english, sub_map)
        if names == 'all':
            pos = pos + sub_pos if sub_pos else pos
        else:
            pos = sub_pos,
    name = pos if names == 'all' else pos[-1]
    logger.debug("Part of speech name found: '{}'".format(name))
    return name