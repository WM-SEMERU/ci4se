def _group_by_batches(samples, check_fn):
    batch_groups = collections.defaultdict(list)
    singles = []
    out_retrieve = []
    extras = []
    for data in [x[0] for x in samples]:
        if check_fn(data):
            batch = tz.get_in(['metadata', 'batch'], data)
            name = str(dd.get_sample_name(data))
            if batch:
                out_retrieve.append((str(batch), data))
            else:
                out_retrieve.append((name, data))
            for vrn in data['variants']:
                if vrn.get('population', True):
                    if batch:
                        batch_groups[str(batch), vrn['variantcaller']].append((
                            vrn['vrn_file'], data))
                    else:
                        singles.append((name, vrn['variantcaller'], data,
                            vrn['vrn_file']))
        else:
            extras.append(data)
    return batch_groups, singles, out_retrieve, extras