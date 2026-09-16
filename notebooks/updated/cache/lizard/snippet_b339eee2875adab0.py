def diff(old, new):
    protocol = new.protocol
    version = new.version
    revision = new.revision
    metric = new.metric
    in_both = _find_unchanged(old.graph, new.graph)
    added_nodes, added_edges = _make_diff(old.graph, new.graph, in_both)
    removed_nodes, removed_edges = _make_diff(new.graph, old.graph, in_both)
    changed_edges = _find_changed(old.graph, new.graph, in_both)
    if added_nodes.nodes() or added_edges.edges():
        added = _netjson_networkgraph(protocol, version, revision, metric,
            added_nodes.nodes(data=True), added_edges.edges(data=True),
            dict=True)
    else:
        added = None
    if removed_nodes.nodes() or removed_edges.edges():
        removed = _netjson_networkgraph(protocol, version, revision, metric,
            removed_nodes.nodes(data=True), removed_edges.edges(data=True),
            dict=True)
    else:
        removed = None
    if changed_edges:
        changed = _netjson_networkgraph(protocol, version, revision, metric,
            [], changed_edges, dict=True)
    else:
        changed = None
    return OrderedDict((('added', added), ('removed', removed), ('changed',
        changed)))