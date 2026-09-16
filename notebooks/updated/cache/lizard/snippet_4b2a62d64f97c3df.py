def _timestamp_instants_eq(a, b):
    assert isinstance(a, datetime)
    if not isinstance(b, datetime):
        return False
    if a.tzinfo is None:
        a = a.replace(tzinfo=OffsetTZInfo())
    if b.tzinfo is None:
        b = b.replace(tzinfo=OffsetTZInfo())
    return a == b