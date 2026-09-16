def list_traces(self, project_id, view=None, page_size=None, start_time=
    None, end_time=None, filter_=None, order_by=None, page_token=None):
    page_iter = self._gapic_api.list_traces(project_id=project_id, view=
        view, page_size=page_size, start_time=start_time, end_time=end_time,
        filter_=filter_, order_by=order_by)
    page_iter.item_to_value = _item_to_mapping
    page_iter.next_page_token = page_token
    return page_iter