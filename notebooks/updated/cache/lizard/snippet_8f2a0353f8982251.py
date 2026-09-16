def lines_by_attribute(self, attr_val=None, attr='type'):
    lines_attributes = nx.get_edge_attributes(self, attr).items()
    if attr_val:
        lines_attributes = [(k, self[k[0]][k[1]]['line']) for k, v in
            lines_attributes if v == attr_val]
    else:
        lines_attributes = [(k, self[k[0]][k[1]]['line']) for k, v in
            lines_attributes]
    lines_sorted = sorted(list(lines_attributes), key=lambda _: repr(_[1]))
    for line in lines_sorted:
        yield {'adj_nodes': line[0], 'line': line[1]}