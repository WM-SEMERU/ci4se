def recursion_depth(key):
    try:
        if not getattr(RECURSION_LEVEL_DICT, 'key', False):
            RECURSION_LEVEL_DICT.key = 0
        RECURSION_LEVEL_DICT.key += 1
        yield RECURSION_LEVEL_DICT.key
        RECURSION_LEVEL_DICT.key -= 1
    except Exception as e:
        RECURSION_LEVEL_DICT.key = 0
        raise e