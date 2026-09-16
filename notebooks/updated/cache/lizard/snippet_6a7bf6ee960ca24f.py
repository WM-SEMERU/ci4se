def __get_aws_metric(table_name, lookback_window_start, lookback_period,
    metric_name):
    try:
        now = datetime.utcnow()
        start_time = now - timedelta(minutes=lookback_window_start)
        end_time = now - timedelta(minutes=lookback_window_start -
            lookback_period)
        return cloudwatch_connection.get_metric_statistics(period=
            lookback_period * 60, start_time=start_time, end_time=end_time,
            metric_name=metric_name, namespace='AWS/DynamoDB', statistics=[
            'Sum'], dimensions={'TableName': table_name}, unit='Count')
    except BotoServerError as error:
        logger.error(
            'Unknown boto error. Status: "{0}". Reason: "{1}". Message: {2}'
            .format(error.status, error.reason, error.message))
        raise