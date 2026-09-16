def get_current_context():
    local_context = _local.get_local_context()
    if local_context.registry:
        return local_context.registry[-1]
    raise errors.NotInContextError('Not in a Context.')