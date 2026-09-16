def linestring_node_to_line(node, with_depth=False):
    assert 'LineString' in node.tag
    crds = [float(x) for x in node.nodes[0].text.split()]
    if with_depth:
        return Line([Point(crds[iloc], crds[iloc + 1], crds[iloc + 2]) for
            iloc in range(0, len(crds), 3)])
    else:
        return Line([Point(crds[iloc], crds[iloc + 1]) for iloc in range(0,
            len(crds), 2)])