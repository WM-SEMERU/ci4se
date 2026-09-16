def _validate_complex_fault_geometry(self, node, _float_re):
    valid_edges = []
    for edge_node in node.nodes:
        try:
            coords = split_coords_3d(edge_node.LineString.posList.text)
            edge = geo.Line([geo.Point(*p) for p in coords])
        except ValueError:
            edge = []
        if len(edge):
            valid_edges.append(True)
        else:
            valid_edges.append(False)
    if node['spacing'] and all(valid_edges):
        return
    raise LogicTreeError(node, self.filename,
        "'complexFaultGeometry' node is not valid")