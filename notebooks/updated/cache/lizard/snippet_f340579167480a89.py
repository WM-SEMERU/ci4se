def apply_t0_nb(times, dom_ids, channel_ids, lookup_tables):
    dom_id = 0
    lookup = np.empty((31, 9))
    for i in range(len(times)):
        cur_dom_id = dom_ids[i]
        if cur_dom_id != dom_id:
            dom_id = cur_dom_id
            for d, m in lookup_tables:
                if d == dom_id:
                    np.copyto(lookup, m)
        t0 = lookup[channel_ids[i]][6]
        times[i] += t0