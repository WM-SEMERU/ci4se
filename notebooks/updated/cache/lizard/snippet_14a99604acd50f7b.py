def deactivate_object(brain_or_object):
    obj = get_object(brain_or_object)
    if is_root(obj):
        fail(401, 'Deactivating the Portal is not allowed')
    try:
        do_transition_for(brain_or_object, 'deactivate')
    except Unauthorized:
        fail(401, "Not allowed to deactivate object '%s'" % obj.getId())