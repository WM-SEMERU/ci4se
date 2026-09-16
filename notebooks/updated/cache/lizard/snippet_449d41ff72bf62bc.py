def to_etree(self):
    nodes_attrib_val = ' '.join('//@nodes.{}'.format(node_id) for node_id in
        self.nodes)
    edges_attrib_val = ' '.join('//@edges.{}'.format(edge_id) for edge_id in
        self.edges)
    attribs = {'{{{pre}}}type'.format(pre=NAMESPACES['xsi']): self.xsi_type,
        'nodes': nodes_attrib_val, 'edges': edges_attrib_val}
    non_empty_attribs = {key: val for key, val in attribs.items() if val is not
        None}
    E = ElementMaker()
    layer = E('layers', non_empty_attribs)
    label_elements = (label.to_etree() for label in self.labels)
    layer.extend(label_elements)
    return layer