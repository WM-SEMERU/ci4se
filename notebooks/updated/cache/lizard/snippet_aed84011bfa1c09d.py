def ReadAllFlowObjects(self, client_id=None, min_create_time=None,
    max_create_time=None, include_child_flows=True):
    res = []
    for flow in itervalues(self.flows):
        if (client_id is None or flow.client_id == client_id) and (
            min_create_time is None or flow.create_time >= min_create_time
            ) and (max_create_time is None or flow.create_time <=
            max_create_time) and (include_child_flows or not flow.
            parent_flow_id):
            res.append(flow.Copy())
    return res