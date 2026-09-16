def _table_attrs(table):
    cmd = ['osqueryi'] + ['--json'] + ['pragma table_info({0})'.format(table)]
    res = __salt__['cmd.run_all'](cmd)
    if res['retcode'] == 0:
        attrs = []
        text = salt.utils.json.loads(res['stdout'])
        for item in text:
            attrs.append(item['name'])
        return attrs
    return False