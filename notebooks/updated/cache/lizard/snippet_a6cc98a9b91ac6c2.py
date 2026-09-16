def import_intermediate_throw_event_to_graph(diagram_graph, process_id,
    process_attributes, element):
    intermediate_throw_event_definitions = {'messageEventDefinition',
        'signalEventDefinition', 'escalationEventDefinition',
        'compensateEventDefinition'}
    BpmnDiagramGraphImport.import_flow_node_to_graph(diagram_graph,
        process_id, process_attributes, element)
    BpmnDiagramGraphImport.import_event_definition_elements(diagram_graph,
        element, intermediate_throw_event_definitions)