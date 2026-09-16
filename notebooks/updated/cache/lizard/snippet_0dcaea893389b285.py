def set_is_polling(polling, host=None, core_name=None):
    ret = _get_return_dict()
    if _is_master() and _get_none_or_value(host) is None:
        err = ['solr.set_is_polling can only be called by "slave" minions']
        return ret.update({'success': False, 'errors': err})
    cmd = 'enablepoll' if polling else 'disapblepoll'
    if _get_none_or_value(core_name) is None and _check_for_cores():
        success = True
        for name in __opts__['solr.cores']:
            resp = set_is_polling(cmd, host=host, core_name=name)
            if not resp['success']:
                success = False
            data = {name: {'data': resp['data']}}
            ret = _update_return_dict(ret, success, data, resp['errors'],
                resp['warnings'])
        return ret
    else:
        resp = _replication_request(cmd, host=host, core_name=core_name)
        return resp