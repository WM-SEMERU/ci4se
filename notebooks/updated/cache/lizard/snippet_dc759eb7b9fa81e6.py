def output_paas(gandi, paas, datacenters, vhosts, output_keys, justify=11):
    output_generic(gandi, paas, output_keys, justify)
    if 'sftp_server' in output_keys:
        output_line(gandi, 'sftp_server', paas['ftp_server'], justify)
    if 'vhost' in output_keys:
        for entry in vhosts:
            output_line(gandi, 'vhost', entry, justify)
    if 'dc' in output_keys:
        dc_name = paas['datacenter'].get('dc_code', paas['datacenter'].get(
            'iso', ''))
        output_line(gandi, 'datacenter', dc_name, justify)
    if 'df' in paas:
        df = paas['df']
        total = df['free'] + df['used']
        if total:
            disk_used = '%.1f%%' % (df['used'] * 100 / total)
            output_line(gandi, 'quota used', disk_used, justify)
    if 'snapshot' in output_keys:
        val = None
        if paas['snapshot_profile']:
            val = paas['snapshot_profile']['name']
        output_line(gandi, 'snapshot', val, justify)
    if 'cache' in paas:
        cache = paas['cache']
        total = cache['hit'] + cache['miss'] + cache['not'] + cache['pass']
        if total:
            output_line(gandi, 'cache', None, justify)
            for key in sorted(cache):
                str_value = '%.1f%%' % (cache[key] * 100 / total)
                output_sub_line(gandi, key, str_value, 5)