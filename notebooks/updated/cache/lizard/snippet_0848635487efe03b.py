def WriteClientActionRequests(self, requests):
    for r in requests:
        req_dict = self.flow_requests.get((r.client_id, r.flow_id), {})
        if r.request_id not in req_dict:
            request_keys = [(r.client_id, r.flow_id, r.request_id) for r in
                requests]
            raise db.AtLeastOneUnknownRequestError(request_keys)
    for r in requests:
        request_key = r.client_id, r.flow_id, r.request_id
        self.client_action_requests[request_key] = r