def list_traces(self, project_id=None, view=None, page_size=None,
    start_time=None, end_time=None, filter_=None, order_by=None, page_token
    =None):
    if project_id is None:
        project_id = self.project
    if start_time is not None:
        start_time = _datetime_to_pb_timestamp(start_time)
    if end_time is not None:
        end_time = _datetime_to_pb_timestamp(end_time)
    return self.trace_api.list_traces(project_id=project_id, view=view,
        page_size=page_size, start_time=start_time, end_time=end_time,
        filter_=filter_, order_by=order_by, page_token=page_token)