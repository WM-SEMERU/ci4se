def truncate_rationale(rationale, max_length=MAX_RATIONALE_SIZE_IN_EVENT):
    if isinstance(rationale, basestring) and max_length is not None and len(
        rationale) > max_length:
        return rationale[0:max_length], True
    else:
        return rationale, False