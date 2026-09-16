def export_data(self, directory, filename, with_md5_hash=False):
    model_data = []
    for est in self.estimators:
        model_data.append({'childrenLeft': est.tree_.children_left.tolist(),
            'childrenRight': est.tree_.children_right.tolist(),
            'thresholds': est.tree_.threshold.tolist(), 'classes': [e[0] for
            e in est.tree_.value.tolist()], 'indices': est.tree_.feature.
            tolist()})
    encoder.FLOAT_REPR = lambda o: self.repr(o)
    json_data = dumps(model_data, sort_keys=True)
    if with_md5_hash:
        import hashlib
        json_hash = hashlib.md5(json_data).hexdigest()
        filename = filename.split('.json')[0] + '_' + json_hash + '.json'
    path = os.path.join(directory, filename)
    with open(path, 'w') as fp:
        fp.write(json_data)