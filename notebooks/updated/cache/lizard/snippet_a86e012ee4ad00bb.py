def _TerminateFlow(rdf_flow, reason=None, flow_state=rdf_flow_objects.Flow.
    FlowState.ERROR):
    flow_cls = registry.FlowRegistry.FlowClassByName(rdf_flow.flow_class_name)
    flow_obj = flow_cls(rdf_flow)
    if not flow_obj.IsRunning():
        return
    logging.info('Terminating flow %s on %s, reason: %s', rdf_flow.flow_id,
        rdf_flow.client_id, reason)
    rdf_flow.flow_state = flow_state
    rdf_flow.error_message = reason
    flow_obj.NotifyCreatorOfError()
    data_store.REL_DB.UpdateFlow(rdf_flow.client_id, rdf_flow.flow_id,
        flow_obj=rdf_flow, processing_on=None, processing_since=None,
        processing_deadline=None)
    data_store.REL_DB.DeleteAllFlowRequestsAndResponses(rdf_flow.client_id,
        rdf_flow.flow_id)