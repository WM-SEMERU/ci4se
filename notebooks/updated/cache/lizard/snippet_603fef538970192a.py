def add_data_flow(self, from_state_id, from_data_port_id, to_state_id,
    to_data_port_id, data_flow_id=None):
    data_flow_id = self.check_data_flow_id(data_flow_id)
    self.data_flows[data_flow_id] = DataFlow(from_state_id,
        from_data_port_id, to_state_id, to_data_port_id, data_flow_id, self)
    return data_flow_id