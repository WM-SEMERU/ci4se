def get_feature_order_constraints(container_dir):
    import json
    file_path = os.path.join(container_dir,
        '_lib/featuremodel/productline/feature_order.json')
    with open(file_path, 'r') as f:
        ordering_constraints = json.loads(f.read())
    return ordering_constraints