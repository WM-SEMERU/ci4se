def remove_binding(name, site, hostheader='', ipaddress='*', port=80):
    ret = {'name': name, 'changes': {}, 'comment': str(), 'result': None}
    binding_info = _get_binding_info(hostheader, ipaddress, port)
    current_bindings = __salt__['win_iis.list_bindings'](site)
    if binding_info not in current_bindings:
        ret['comment'] = 'Binding has already been removed: {0}'.format(
            binding_info)
        ret['result'] = True
    elif __opts__['test']:
        ret['comment'] = 'Binding will be removed: {0}'.format(binding_info)
        ret['changes'] = {'old': binding_info, 'new': None}
    else:
        ret['comment'] = 'Removed binding: {0}'.format(binding_info)
        ret['changes'] = {'old': binding_info, 'new': None}
        ret['result'] = __salt__['win_iis.remove_binding'](site, hostheader,
            ipaddress, port)
    return ret