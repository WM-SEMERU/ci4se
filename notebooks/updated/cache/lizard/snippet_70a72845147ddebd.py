def get_special_inds(sample, label_store, aux_note):
    s0_inds = np.where(sample == np.int64(0))[0]
    note_inds = np.where(label_store == np.int64(22))[0]
    potential_definition_inds = set(s0_inds).intersection(note_inds)
    notann_inds = np.where(label_store == np.int64(0))[0]
    rm_inds = potential_definition_inds.union(set(notann_inds))
    return potential_definition_inds, rm_inds