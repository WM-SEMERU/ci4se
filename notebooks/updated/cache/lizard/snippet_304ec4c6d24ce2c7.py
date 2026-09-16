def add_response_log_fields(self, log_fields: LogFields, start_time:
    datetime, err: Exception):
    code = 'Unknown' if err is not None else 'OK'
    duration = (datetime.utcnow() - start_time).total_seconds() * 1000
    log_fields.add_fields({'grpc.start_time': start_time.isoformat() + 'Z',
        'grpc.code': code, 'duration': '{duration}ms'.format(duration=
        duration)})