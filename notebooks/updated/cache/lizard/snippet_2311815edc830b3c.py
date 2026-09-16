def logging_levels(name, remote=None, local=None):
    ret = _default_ret(name)
    syslog_conf = __salt__['cimc.get_syslog_settings']()
    req_change = False
    try:
        syslog_dict = syslog_conf['outConfigs']['commSyslog'][0]
        if remote and syslog_dict['remoteSeverity'] != remote:
            req_change = True
        elif local and syslog_dict['localSeverity'] != local:
            req_change = True
        if req_change:
            update = __salt__['cimc.set_logging_levels'](remote, local)
            if update['outConfig']['commSyslog'][0]['status'] != 'modified':
                ret['result'] = False
                ret['comment'] = 'Error setting logging levels.'
                return ret
            ret['changes']['before'] = syslog_conf
            ret['changes']['after'] = __salt__['cimc.get_syslog_settings']()
            ret['comment'] = 'Logging level settings modified.'
        else:
            ret['comment'
                ] = 'Logging level already configured. No changes required.'
    except Exception as err:
        ret['result'] = False
        ret['comment'] = 'Error occurred setting logging level settings.'
        log.error(err)
        return ret
    ret['result'] = True
    return ret