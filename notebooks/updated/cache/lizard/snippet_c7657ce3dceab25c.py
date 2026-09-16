def from_json(cls, json):
    num_ranges = int(json['num_ranges'])
    query_spec = json['query_spec']
    item_name = json['item_name']
    p_range_iters = []
    for i in xrange(num_ranges):
        json_item = json[str(i)]
        json_item['query_spec'] = query_spec
        json_item['name'] = item_name
        p_range_iters.append(_PropertyRangeModelIterator.from_json(json_item))
    obj = cls(p_range_iters)
    return obj