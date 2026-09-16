def process_json(json_dict):
    ep = EidosProcessor(json_dict)
    ep.extract_causal_relations()
    ep.extract_correlations()
    ep.extract_events()
    return ep