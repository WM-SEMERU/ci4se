def runner(name, **kwargs):
    try:
        jid = __orchestration_jid__
    except NameError:
        log.debug(
            'Unable to fire args event due to missing __orchestration_jid__')
        jid = None
    if __opts__.get('test', False):
        ret = {'name': name, 'result': None, 'changes': {}, 'comment':
            "Runner function '{0}' would be executed.".format(name)}
        return ret
    out = __salt__['saltutil.runner'](name, __orchestration_jid__=jid,
        __env__=__env__, full_return=True, **kwargs)
    if kwargs.get('asynchronous'):
        out['return'] = out.copy()
        out['success'] = 'jid' in out and 'tag' in out
    runner_return = out.get('return')
    if isinstance(runner_return, dict) and 'Error' in runner_return:
        out['success'] = False
    success = out.get('success', True)
    ret = {'name': name, 'changes': {'return': runner_return}, 'result':
        success}
    ret['comment'] = "Runner function '{0}' {1}.".format(name, 'executed' if
        success else 'failed')
    ret['__orchestration__'] = True
    if 'jid' in out:
        ret['__jid__'] = out['jid']
    return ret