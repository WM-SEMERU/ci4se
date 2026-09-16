def get_eids(rup_array, samples_by_grp, num_rlzs_by_grp):
    all_eids = []
    for rup in rup_array:
        grp_id = rup['grp_id']
        samples = samples_by_grp[grp_id]
        num_rlzs = num_rlzs_by_grp[grp_id]
        num_events = rup['n_occ'] if samples > 1 else rup['n_occ'] * num_rlzs
        eids = TWO32 * U64(rup['serial']) + numpy.arange(num_events, dtype=U64)
        all_eids.append(eids)
    return numpy.concatenate(all_eids)