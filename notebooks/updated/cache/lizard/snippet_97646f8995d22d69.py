def filter_log_events(awsclient, log_group_name, start_ts, end_ts=None):
    client_logs = awsclient.get_client('logs')
    logs = []
    next_token = None
    while True:
        request = {'logGroupName': log_group_name, 'startTime': start_ts}
        if end_ts:
            request['endTime'] = end_ts
        if next_token:
            request['nextToken'] = next_token
        response = client_logs.filter_log_events(**request)
        logs.extend([{'timestamp': e['timestamp'], 'message': e['message']} for
            e in response['events']])
        if 'nextToken' not in response:
            break
        next_token = response['nextToken']
    return logs