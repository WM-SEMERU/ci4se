def _build_service_livestate(self, host_name, service_name, livestate):
    state = livestate.get('state', 'OK').upper()
    output = livestate.get('output', '')
    long_output = livestate.get('long_output', '')
    perf_data = livestate.get('perf_data', '')
    try:
        timestamp = int(livestate.get('timestamp', 'ABC'))
    except ValueError:
        timestamp = None
    service_state_to_id = {'OK': 0, 'WARNING': 1, 'CRITICAL': 2, 'UNKNOWN':
        3, 'UNREACHABLE': 4}
    parameters = '%s;%s' % (service_state_to_id.get(state, 3), output)
    if long_output and perf_data:
        parameters = '%s|%s\n%s' % (parameters, perf_data, long_output)
    elif long_output:
        parameters = '%s\n%s' % (parameters, long_output)
    elif perf_data:
        parameters = '%s|%s' % (parameters, perf_data)
    command_line = 'PROCESS_SERVICE_CHECK_RESULT;%s;%s;%s' % (host_name,
        service_name, parameters)
    if timestamp is not None:
        command_line = '[%d] %s' % (timestamp, command_line)
    else:
        command_line = '[%d] %s' % (int(time.time()), command_line)
    return command_line