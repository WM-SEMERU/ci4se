def lambda_handler(event, context):
    event = json.loads(gzip.GzipFile(fileobj=StringIO(event['awslogs'][
        'data'].decode('base64'))).read())
    account = event['owner']
    region = context.invoked_function_arn.split(':', 4)[3]
    log_events = event['logEvents']
    for log_event in log_events:
        message = json.loads(log_event['message'])
        ts = log_event['timestamp'] / 1000
        _process_rds_enhanced_monitoring_message(ts, message, account, region)
    stats.flush()
    return {'Status': 'OK'}