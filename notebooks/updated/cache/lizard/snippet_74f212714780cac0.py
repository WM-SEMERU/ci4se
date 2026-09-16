def flush(table='filter', chain='', family='ipv4'):
    wait = '--wait' if _has_option('--wait', family) else ''
    cmd = '{0} {1} -t {2} -F {3}'.format(_iptables_cmd(family), wait, table,
        chain)
    out = __salt__['cmd.run'](cmd)
    return out