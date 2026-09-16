def UpdateHuntObject(self, hunt_id, duration=None, client_rate=None,
    client_limit=None, hunt_state=None, hunt_state_comment=None, start_time
    =None, num_clients_at_start_time=None):
    _ValidateHuntId(hunt_id)
    precondition.AssertOptionalType(duration, rdfvalue.Duration)
    precondition.AssertOptionalType(client_rate, (float, int))
    precondition.AssertOptionalType(client_limit, int)
    if hunt_state is not None:
        _ValidateEnumType(hunt_state, rdf_hunt_objects.Hunt.HuntState)
    precondition.AssertOptionalType(hunt_state_comment, str)
    precondition.AssertOptionalType(start_time, rdfvalue.RDFDatetime)
    precondition.AssertOptionalType(num_clients_at_start_time, int)
    return self.delegate.UpdateHuntObject(hunt_id, duration=duration,
        client_rate=client_rate, client_limit=client_limit, hunt_state=
        hunt_state, hunt_state_comment=hunt_state_comment, start_time=
        start_time, num_clients_at_start_time=num_clients_at_start_time)