def HandleWellKnownFlows(self, messages):
    msgs_by_wkf = {}
    result = []
    for msg in messages:
        if msg.response_id != 0:
            result.append(msg)
            continue
        flow_name = msg.session_id.FlowName()
        if flow_name in self.well_known_flows:
            msgs_by_wkf.setdefault(flow_name, []).append(msg)
            stats_collector_instance.Get().IncrementCounter(
                'grr_well_known_flow_requests')
            stats_collector_instance.Get().IncrementCounter(
                'well_known_flow_requests', fields=[str(msg.session_id)])
        else:
            msg.response_id = random.UInt32()
            result.append(msg)
    for flow_name, msg_list in iteritems(msgs_by_wkf):
        wkf = self.well_known_flows[flow_name]
        wkf.ProcessMessages(msg_list)
    return result