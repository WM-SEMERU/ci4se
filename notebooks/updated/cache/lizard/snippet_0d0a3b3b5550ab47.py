def features_keep_by_property(obj, query):
    features_keep = []
    for feature in tqdm(obj['features']):
        if all([match(feature['properties'].get(prop), qry) for prop, qry in
            query.items()]):
            features_keep.append(feature)
    obj['features'] = features_keep
    return obj