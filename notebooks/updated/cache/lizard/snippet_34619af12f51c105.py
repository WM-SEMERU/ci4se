def validate_argmin_with_skipna(skipna, args, kwargs):
    skipna, args = process_skipna(skipna, args)
    validate_argmin(args, kwargs)
    return skipna