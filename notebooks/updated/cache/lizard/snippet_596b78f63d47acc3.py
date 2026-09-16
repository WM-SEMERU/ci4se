def export_start_event(bpmn_graph, export_elements, node,
    nodes_classification, order=0, prefix='', condition='', who=''):
    event_definitions = node[1].get(consts.Consts.event_definitions)
    if event_definitions is not None and len(event_definitions) > 0:
        event_definition = node[1][consts.Consts.event_definitions][0]
    else:
        event_definition = None
    if event_definition is None:
        activity = node[1][consts.Consts.node_name]
    elif event_definition[consts.Consts.definition_type
        ] == 'messageEventDefinition':
        activity = 'message ' + node[1][consts.Consts.node_name]
    elif event_definition[consts.Consts.definition_type
        ] == 'timerEventDefinition':
        activity = 'timer ' + node[1][consts.Consts.node_name]
    else:
        activity = node[1][consts.Consts.node_name]
    export_elements.append({'Order': prefix + str(order), 'Activity':
        activity, 'Condition': condition, 'Who': who, 'Subprocess': '',
        'Terminated': ''})
    outgoing_flow_id = node[1][consts.Consts.outgoing_flow][0]
    outgoing_flow = bpmn_graph.get_flow_by_id(outgoing_flow_id)
    outgoing_node = bpmn_graph.get_node_by_id(outgoing_flow[2][consts.
        Consts.target_ref])
    return BpmnDiagramGraphCsvExport.export_node(bpmn_graph,
        export_elements, outgoing_node, nodes_classification, order + 1,
        prefix, who)