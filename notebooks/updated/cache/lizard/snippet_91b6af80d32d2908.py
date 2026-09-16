def update(dest, variation, path=None):
    if dest is None:
        return None
    if variation is None:
        return dest
    if path is None:
        path = []
    for key in variation:
        if key in dest:
            if isinstance(dest[key], dict) and isinstance(variation[key], dict
                ):
                EBUtils.update(dest[key], variation[key], path + [str(key)])
            elif dest[key] == variation[key]:
                pass
            else:
                dest[key] = variation[key]
        else:
            dest[key] = variation[key]
    return dest