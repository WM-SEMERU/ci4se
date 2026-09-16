def cli(name, format='text', **kwargs):
    ret = {'name': name, 'changes': {}, 'result': True, 'comment': ''}
    ret['changes'] = __salt__['junos.cli'](name, format, **kwargs)
    return ret