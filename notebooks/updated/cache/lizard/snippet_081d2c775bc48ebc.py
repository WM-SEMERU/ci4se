def get_jobs(state='all'):
    if state.lower() == 'all':
        query = {'type': 'op', 'cmd': '<show><jobs><all></all></jobs></show>'}
    elif state.lower() == 'pending':
        query = {'type': 'op', 'cmd':
            '<show><jobs><pending></pending></jobs></show>'}
    elif state.lower() == 'processed':
        query = {'type': 'op', 'cmd':
            '<show><jobs><processed></processed></jobs></show>'}
    else:
        raise CommandExecutionError(
            'The state parameter must be all, pending, or processed.')
    return __proxy__['panos.call'](query)