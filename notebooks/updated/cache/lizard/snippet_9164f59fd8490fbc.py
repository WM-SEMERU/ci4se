def get_properties_from_graph(graph):
    property_set = set()
    for row in graph.predicates():
        property_set.add(row)
    return property_set