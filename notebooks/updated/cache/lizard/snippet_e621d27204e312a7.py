def export_lane_set(process, lane_set, plane_element):
    lane_set_xml = eTree.SubElement(process, consts.Consts.lane_set)
    for key, value in lane_set[consts.Consts.lanes].items():
        BpmnDiagramGraphExport.export_lane(lane_set_xml, key, value,
            plane_element)