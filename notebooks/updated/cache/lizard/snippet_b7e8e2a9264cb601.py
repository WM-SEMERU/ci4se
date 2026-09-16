def _append_request_ids(self, resp):
    if isinstance(resp, list):
        for resp_obj in resp:
            self._append_request_id(resp_obj)
    elif resp is not None:
        self._append_request_id(resp)