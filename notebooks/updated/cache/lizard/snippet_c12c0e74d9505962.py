def _enum_from_direction(direction):
    if isinstance(direction, int):
        return direction
    if direction == Query.ASCENDING:
        return enums.StructuredQuery.Direction.ASCENDING
    elif direction == Query.DESCENDING:
        return enums.StructuredQuery.Direction.DESCENDING
    else:
        msg = _BAD_DIR_STRING.format(direction, Query.ASCENDING, Query.
            DESCENDING)
        raise ValueError(msg)