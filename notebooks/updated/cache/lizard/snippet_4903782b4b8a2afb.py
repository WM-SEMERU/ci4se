def request_data_stream_send(self, target_system, target_component,
    req_stream_id, req_message_rate, start_stop, force_mavlink1=False):
    return self.send(self.request_data_stream_encode(target_system,
        target_component, req_stream_id, req_message_rate, start_stop),
        force_mavlink1=force_mavlink1)