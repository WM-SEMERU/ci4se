def squash(change, is_ignored=False, options=None):
    if options:
        is_ignored = change.is_ignored(options)
    if isinstance(change, Removal):
        result = SquashedRemoval(change, is_ignored)
    elif isinstance(change, Addition):
        result = SquashedAddition(change, is_ignored)
    else:
        result = SquashedChange(change, is_ignored)
    return result