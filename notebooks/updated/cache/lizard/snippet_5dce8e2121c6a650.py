def ParseAgeSpecification(cls, age):
    try:
        return 0, int(age)
    except (ValueError, TypeError):
        pass
    if age == NEWEST_TIME:
        return data_store.DB.NEWEST_TIMESTAMP
    elif age == ALL_TIMES:
        return data_store.DB.ALL_TIMESTAMPS
    elif len(age) == 2:
        start, end = age
        return int(start), int(end)
    raise ValueError('Unknown age specification: %s' % age)