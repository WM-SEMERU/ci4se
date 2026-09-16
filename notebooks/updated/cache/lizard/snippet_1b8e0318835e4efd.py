def new_chain(table='filter', chain=None, table_type=None, hook=None,
    priority=None, family='ipv4'):
    ret = {'comment': '', 'result': False}
    if not chain:
        ret['comment'] = 'Chain needs to be specified'
        return ret
    res = check_table(table, family=family)
    if not res['result']:
        return res
    res = check_chain(table, chain, family=family)
    if res['result']:
        ret['comment'
            ] = 'Chain {0} in table {1} in family {2} already exists'.format(
            chain, table, family)
        return ret
    nft_family = _NFTABLES_FAMILIES[family]
    cmd = '{0} add chain {1} {2} {3}'.format(_nftables_cmd(), nft_family,
        table, chain)
    if table_type or hook or priority:
        if table_type and hook and six.text_type(priority):
            cmd = '{0} \\{{ type {1} hook {2} priority {3}\\; \\}}'.format(cmd,
                table_type, hook, priority)
        else:
            ret['comment'] = 'Table_type, hook, and priority required.'
            return ret
    out = __salt__['cmd.run'](cmd, python_shell=False)
    if not out:
        ret['comment'] = 'Chain {0} in table {1} in family {2} created'.format(
            chain, table, family)
        ret['result'] = True
    else:
        ret['comment'
            ] = 'Chain {0} in table {1} in family {2} could not be created'.format(
            chain, table, family)
    return ret