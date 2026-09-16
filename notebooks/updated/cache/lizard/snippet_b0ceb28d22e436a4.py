def from_payload(self, payload):
    self.session_id = payload[0] * 256 + payload[1]
    self.originator = Originator(payload[2])
    self.priority = Priority(payload[3])
    len_node_ids = payload[41]
    if len_node_ids > 20:
        raise PyVLXException('command_send_request_wrong_node_length')
    self.node_ids = []
    for i in range(len_node_ids):
        self.node_ids.append(payload[42] + i)
    self.parameter = Parameter(payload[7:9])