def reloaded(name, jboss_config, timeout=60, interval=5):
    log.debug(' ======================== STATE: jboss7.reloaded (name: %s) ',
        name)
    ret = {'name': name, 'result': True, 'changes': {}, 'comment': ''}
    status = __salt__['jboss7.status'](jboss_config)
    if not status['success'] or status['result'] not in ('running',
        'reload-required'):
        ret['result'] = False
        ret['comment'] = (
            "Cannot reload server configuration, it should be up and in 'running' or 'reload-required' state."
            )
        return ret
    result = __salt__['jboss7.reload'](jboss_config)
    if (result['success'] or 'Operation failed: Channel closed' in result[
        'stdout'] or 
        'Communication error: java.util.concurrent.ExecutionException: Operation failed'
         in result['stdout']):
        wait_time = 0
        status = None
        while (status is None or not status['success'] or status['result'] !=
            'running') and wait_time < timeout:
            time.sleep(interval)
            wait_time += interval
            status = __salt__['jboss7.status'](jboss_config)
        if status['success'] and status['result'] == 'running':
            ret['result'] = True
            ret['comment'] = 'Configuration reloaded'
            ret['changes']['reloaded'] = 'configuration'
        else:
            ret['result'] = False
            ret['comment'] = (
                'Could not reload the configuration. Timeout ({0} s) exceeded. '
                .format(timeout))
            if not status['success']:
                ret['comment'] = __append_comment(
                    'Could not connect to JBoss controller.', ret['comment'])
            else:
                ret['comment'] = __append_comment('Server is in {0} state'.
                    format(status['result']), ret['comment'])
    else:
        ret['result'] = False
        ret['comment'
            ] = 'Could not reload the configuration, stdout:' + result['stdout'
            ]
    return ret