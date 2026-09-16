def value_present(name, xpath, value, **kwargs):
    ret = {'name': name, 'changes': {}, 'result': True, 'comment': ''}
    if 'test' not in kwargs:
        kwargs['test'] = __opts__.get('test', False)
    current_value = __salt__['xml.get_value'](name, xpath)
    if not current_value:
        ret['result'] = False
        ret['comment'] = 'xpath query {0} not found in {1}'.format(xpath, name)
        return ret
    if current_value != value:
        if kwargs['test']:
            ret['result'] = None
            ret['comment'] = '{0} will be updated'.format(name)
            ret['changes'] = {name: {'old': current_value, 'new': value}}
        else:
            results = __salt__['xml.set_value'](name, xpath, value)
            ret['result'] = results
            ret['comment'] = '{0} updated'.format(name)
            ret['changes'] = {name: {'old': current_value, 'new': value}}
    else:
        ret['comment'] = '{0} is already present'.format(value)
    return ret