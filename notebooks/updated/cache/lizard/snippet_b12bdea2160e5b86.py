def lucene_version(core_name=None):
    ret = _get_return_dict()
    if _get_none_or_value(core_name) is None and _check_for_cores():
        success = True
        for name in __salt__['config.option']('solr.cores'):
            resp = _get_admin_info('system', core_name=name)
            if resp['success']:
                version_num = resp['data']['lucene']['lucene-spec-version']
                data = {name: {'lucene_version': version_num}}
            else:
                data = {name: {'lucene_version': None}}
                success = False
            ret = _update_return_dict(ret, success, data, resp['errors'])
        return ret
    else:
        resp = _get_admin_info('system', core_name=core_name)
        if resp['success']:
            version_num = resp['data']['lucene']['lucene-spec-version']
            return _get_return_dict(True, {'version': version_num}, resp[
                'errors'])
        else:
            return resp