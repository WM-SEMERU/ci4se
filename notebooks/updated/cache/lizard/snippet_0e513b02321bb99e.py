def inspect(data, look_for=['featuretype', 'chrom', 'attribute_keys',
    'feature_count'], limit=None, verbose=True):
    results = {}
    obj_attrs = []
    for i in look_for:
        if i not in ['attribute_keys', 'feature_count']:
            obj_attrs.append(i)
        results[i] = Counter()
    attr_keys = 'attribute_keys' in look_for
    d = iterators.DataIterator(data)
    feature_count = 0
    for f in d:
        if verbose:
            sys.stderr.write('\r%s features inspected' % feature_count)
            sys.stderr.flush()
        for obj_attr in obj_attrs:
            results[obj_attr].update([getattr(f, obj_attr)])
        if attr_keys:
            results['attribute_keys'].update(f.attributes.keys())
        feature_count += 1
        if limit and feature_count == limit:
            break
    new_results = {}
    for k, v in results.items():
        new_results[k] = dict(v)
    new_results['feature_count'] = feature_count
    return new_results