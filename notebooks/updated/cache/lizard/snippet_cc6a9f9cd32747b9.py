def _HuntFlowCondition(self, condition):
    if condition == db.HuntFlowsCondition.UNSET:
        return '', []
    elif condition == db.HuntFlowsCondition.FAILED_FLOWS_ONLY:
        return 'AND flow_state = %s ', [int(rdf_flow_objects.Flow.FlowState
            .ERROR)]
    elif condition == db.HuntFlowsCondition.SUCCEEDED_FLOWS_ONLY:
        return 'AND flow_state = %s ', [int(rdf_flow_objects.Flow.FlowState
            .FINISHED)]
    elif condition == db.HuntFlowsCondition.COMPLETED_FLOWS_ONLY:
        return 'AND (flow_state = %s OR flow_state = %s) ', [int(
            rdf_flow_objects.Flow.FlowState.FINISHED), int(rdf_flow_objects
            .Flow.FlowState.ERROR)]
    elif condition == db.HuntFlowsCondition.FLOWS_IN_PROGRESS_ONLY:
        return 'AND flow_state = %s ', [int(rdf_flow_objects.Flow.FlowState
            .RUNNING)]
    elif condition == db.HuntFlowsCondition.CRASHED_FLOWS_ONLY:
        return 'AND flow_state = %s ', [int(rdf_flow_objects.Flow.FlowState
            .CRASHED)]
    else:
        raise ValueError('Invalid condition value: %r' % condition)