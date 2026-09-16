def import_lane_set_element(process_attributes, lane_set_element, plane_element
    ):
    lane_set_id = lane_set_element.getAttribute(consts.Consts.id)
    lanes_attr = {}
    for element in utils.BpmnImportUtils.iterate_elements(lane_set_element):
        if element.nodeType != element.TEXT_NODE:
            tag_name = utils.BpmnImportUtils.remove_namespace_from_tag_name(
                element.tagName)
            if tag_name == consts.Consts.lane:
                lane = element
                lane_id = lane.getAttribute(consts.Consts.id)
                lane_attr = BpmnDiagramGraphImport.import_lane_element(lane,
                    plane_element)
                lanes_attr[lane_id] = lane_attr
    lane_set_attr = {consts.Consts.id: lane_set_id, consts.Consts.lanes:
        lanes_attr}
    process_attributes[consts.Consts.lane_set] = lane_set_attr