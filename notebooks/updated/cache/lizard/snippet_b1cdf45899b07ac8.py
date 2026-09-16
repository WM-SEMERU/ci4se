def import_process_elements(document, diagram_graph, sequence_flows,
    process_elements_dict, plane_element):
    for process_element in document.getElementsByTagNameNS('*', consts.
        Consts.process):
        BpmnDiagramGraphImport.import_process_element(process_elements_dict,
            process_element)
        process_id = process_element.getAttribute(consts.Consts.id)
        process_attributes = process_elements_dict[process_id]
        lane_set_list = process_element.getElementsByTagNameNS('*', consts.
            Consts.lane_set)
        if lane_set_list is not None and len(lane_set_list) > 0:
            lane_set = lane_set_list[0]
            BpmnDiagramGraphImport.import_lane_set_element(process_attributes,
                lane_set, plane_element)
        for element in utils.BpmnImportUtils.iterate_elements(process_element):
            if element.nodeType != element.TEXT_NODE:
                tag_name = (utils.BpmnImportUtils.
                    remove_namespace_from_tag_name(element.tagName))
                BpmnDiagramGraphImport.__import_element_by_tag_name(
                    diagram_graph, sequence_flows, process_id,
                    process_attributes, element, tag_name)
        for flow in utils.BpmnImportUtils.iterate_elements(process_element):
            if flow.nodeType != flow.TEXT_NODE:
                tag_name = (utils.BpmnImportUtils.
                    remove_namespace_from_tag_name(flow.tagName))
                if tag_name == consts.Consts.sequence_flow:
                    BpmnDiagramGraphImport.import_sequence_flow_to_graph(
                        diagram_graph, sequence_flows, process_id, flow)