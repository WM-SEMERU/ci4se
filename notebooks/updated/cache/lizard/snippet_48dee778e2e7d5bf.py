def CallState(self, next_state='', start_time=None):
    if not getattr(self, next_state):
        raise ValueError('Next state %s is invalid.' % next_state)
    flow_request = rdf_flow_objects.FlowRequest(client_id=self.rdf_flow.
        client_id, flow_id=self.rdf_flow.flow_id, request_id=self.
        GetNextOutboundId(), next_state=next_state, start_time=start_time,
        needs_processing=True)
    self.flow_requests.append(flow_request)