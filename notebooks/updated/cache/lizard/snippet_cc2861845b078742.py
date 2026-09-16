def absent(name, **kwargs):
    ret = {'name': name, 'changes': {}, 'result': False, 'comment': ''}
    comment_host_deleted = 'Host {0} deleted.'.format(name)
    comment_host_notdeleted = 'Unable to delete host: {0}. '.format(name)
    comment_host_notexists = 'Host {0} does not exist.'.format(name)
    changes_host_deleted = {name: {'old': 'Host {0} exists.'.format(name),
        'new': 'Host {0} deleted.'.format(name)}}
    connection_args = {}
    if '_connection_user' in kwargs:
        connection_args['_connection_user'] = kwargs['_connection_user']
    if '_connection_password' in kwargs:
        connection_args['_connection_password'] = kwargs['_connection_password'
            ]
    if '_connection_url' in kwargs:
        connection_args['_connection_url'] = kwargs['_connection_url']
    host_exists = __salt__['zabbix.host_exists'](name, **connection_args)
    if __opts__['test']:
        if not host_exists:
            ret['result'] = True
            ret['comment'] = comment_host_notexists
        else:
            ret['result'] = None
            ret['comment'] = comment_host_deleted
        return ret
    host_get = __salt__['zabbix.host_get'](name, **connection_args)
    if not host_get:
        ret['result'] = True
        ret['comment'] = comment_host_notexists
    else:
        try:
            hostid = host_get[0]['hostid']
            host_delete = __salt__['zabbix.host_delete'](hostid, **
                connection_args)
        except KeyError:
            host_delete = False
        if host_delete and 'error' not in host_delete:
            ret['result'] = True
            ret['comment'] = comment_host_deleted
            ret['changes'] = changes_host_deleted
        else:
            ret['result'] = False
            ret['comment'] = comment_host_notdeleted + six.text_type(
                host_delete['error'])
    return ret