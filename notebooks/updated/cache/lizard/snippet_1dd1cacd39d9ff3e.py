def republish_module_trigger(plpy, td):
    is_legacy_publication = td['new']['version'] is not None
    if not is_legacy_publication:
        return 'OK'
    plpy.log('Trigger fired on %s' % (td['new']['moduleid'],))
    modified = republish_module(td, plpy)
    plpy.log('modified: {}'.format(modified))
    plpy.log('insert values:\n{}\n'.format('\n'.join(['{}: {}'.format(key,
        value) for key, value in td['new'].items()])))
    return modified