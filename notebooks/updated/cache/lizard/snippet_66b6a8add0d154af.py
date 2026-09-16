def vc_output_record(samples):
    shared_keys = [['vrn_file'], ['validate', 'summary'], ['validate', 'tp'
        ], ['validate', 'fp'], ['validate', 'fn']]
    raw = cwlutils.samples_to_records([utils.to_single_data(x) for x in
        samples])
    shared = {}
    for key in shared_keys:
        cur = list(set([x for x in [tz.get_in(key, d) for d in raw] if x]))
        if len(cur) > 0:
            assert len(cur) == 1, (key, cur)
            shared[tuple(key)] = cur[0]
        else:
            shared[tuple(key)] = None
    out = []
    for d in raw:
        for key, val in shared.items():
            d = tz.update_in(d, key, lambda x: val)
        out.append([d])
    return out