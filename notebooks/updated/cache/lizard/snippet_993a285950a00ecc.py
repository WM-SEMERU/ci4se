def count(procfile):
    u
    state_tcp = {'01': 'ESTABLISHED', '02': 'SYN_SENT', '03': 'SYN_RECV',
        '04': 'FIN_WAIT1', '05': 'FIN_WAIT2', '06': 'TIME_WAIT', '07':
        'CLOSE', '08': 'CLOSE_WAIT', '09': 'LAST_ACK', '0A': 'LISTEN', '0B':
        'CLOSING'}
    protocol = os.path.basename(procfile.name)
    state = []
    stats = {}
    for line in procfile.readlines():
        state.append(line.split()[3])
    for state_type, state_name in state_tcp.items():
        key = 'linux.net.{proto}[{state}]'.format(proto=protocol, state=
            state_name)
        value = state.count(state_type)
        stats[key] = value
    procfile.close()
    return stats