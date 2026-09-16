def normalize_mask(mask, is_micro):
    if mask is None:
        return None
    try:
        mask = int(mask)
    except ValueError:
        raise MaskError(
            'Invalid data mask "{0}". Must be an integer or a string which represents an integer value.'
            .format(mask))
    if is_micro:
        if not 0 <= mask < 4:
            raise MaskError(
                'Invalid data mask "{0}" for Micro QR Code. Must be in range 0 .. 3'
                .format(mask))
    elif not 0 <= mask < 8:
        raise MaskError('Invalid data mask "{0}". Must be in range 0 .. 7'.
            format(mask))
    return mask