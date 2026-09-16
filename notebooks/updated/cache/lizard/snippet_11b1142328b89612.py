def DeleteMessageHandlerRequests(self, requests):
    for r in requests:
        flow_dict = self.message_handler_requests.get(r.handler_name, {})
        if r.request_id in flow_dict:
            del flow_dict[r.request_id]
        flow_dict = self.message_handler_leases.get(r.handler_name, {})
        if r.request_id in flow_dict:
            del flow_dict[r.request_id]