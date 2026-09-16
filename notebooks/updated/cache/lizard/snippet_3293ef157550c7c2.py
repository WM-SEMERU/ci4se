def delete_user(ctx, yes):
    if ctx.obj['username'] is None:
        username = _ask('Please enter username:')
    else:
        username = ctx.obj['username']
    del_user = ctx.obj['db'].objectmodels['user'].find_one({'name': username})
    if yes or _ask('Confirm deletion', default=False, data_type='bool'):
        try:
            del_user.delete()
            log('Done')
        except AttributeError:
            log('User not found', lvl=warn)
    else:
        log('Cancelled')