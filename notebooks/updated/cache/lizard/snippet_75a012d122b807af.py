def ReadHuntFlowsStatesAndTimestamps(self, hunt_id):
    result = []
    for f in self._GetHuntFlows(hunt_id):
        result.append(db.FlowStateAndTimestamps(flow_state=f.flow_state,
            create_time=f.create_time, last_update_time=f.last_update_time))
    return result