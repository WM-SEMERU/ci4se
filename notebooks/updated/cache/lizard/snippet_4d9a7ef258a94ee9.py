def aggregated_records(all_records, key_fields=KEY_FIELDS):
    flow_table = defaultdict(_FlowStats)
    for flow_record in all_records:
        key = tuple(getattr(flow_record, attr) for attr in key_fields)
        if any(x is None for x in key):
            continue
        flow_table[key].update(flow_record)
    for key in flow_table:
        item = {k: v for k, v in zip(key_fields, key)}
        item.update(flow_table[key].to_dict())
        yield item