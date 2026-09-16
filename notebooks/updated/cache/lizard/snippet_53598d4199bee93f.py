def non_transactional(func, args, kwds, allow_existing=True):
    from . import tasklets
    ctx = tasklets.get_context()
    if not ctx.in_transaction():
        return func(*args, **kwds)
    if not allow_existing:
        raise datastore_errors.BadRequestError(
            '%s cannot be called within a transaction.' % func.__name__)
    save_ctx = ctx
    while ctx.in_transaction():
        ctx = ctx._parent_context
        if ctx is None:
            raise datastore_errors.BadRequestError(
                'Context without non-transactional ancestor')
    save_ds_conn = datastore._GetConnection()
    try:
        if hasattr(save_ctx, '_old_ds_conn'):
            datastore._SetConnection(save_ctx._old_ds_conn)
        tasklets.set_context(ctx)
        return func(*args, **kwds)
    finally:
        tasklets.set_context(save_ctx)
        datastore._SetConnection(save_ds_conn)