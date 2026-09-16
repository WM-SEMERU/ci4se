def query_events(resource_root, query_str=None):
    params = None
    if query_str:
        params = dict(query=query_str)
    return call(resource_root.get, EVENTS_PATH, ApiEventQueryResult, params
        =params)