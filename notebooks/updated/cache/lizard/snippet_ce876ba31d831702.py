def _generate_combined_log(self, request, response):
    current_time = datetime.utcnow()
    data_len = '-' if response.data is None else len(response.data)
    return '{0} - - [{1}] {2} {3} {4} {5} {6}'.format(request.remote_addr,
        current_time, request.method, request.relative_uri, response.status,
        data_len, request.user_agent)