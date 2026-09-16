def TNE_metric(bpmn_graph):
    events_counts = get_events_counts(bpmn_graph)
    return sum([count for _, count in events_counts.items()])