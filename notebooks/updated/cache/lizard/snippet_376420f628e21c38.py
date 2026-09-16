def get_logs(self, request):
    project = request.get_project()
    logstore = request.get_logstore()
    from_time = request.get_from()
    to_time = request.get_to()
    topic = request.get_topic()
    query = request.get_query()
    reverse = request.get_reverse()
    offset = request.get_offset()
    size = request.get_line()
    return self.get_log(project, logstore, from_time, to_time, topic, query,
        reverse, offset, size)