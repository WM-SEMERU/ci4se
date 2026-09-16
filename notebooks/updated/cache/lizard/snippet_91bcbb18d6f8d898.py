def _auto_kpath_labels(kpt_list):
    label_i = 1
    kpt_labels = {}
    for kpt in chain(*kpt_list):
        if tuple(kpt) in kpt_labels:
            continue
        else:
            kpt_labels.update({tuple(kpt): '({})'.format(label_i)})
            label_i += 1
    kpath_labels = [[kpt_labels[tuple(kpt)] for kpt in segment] for segment in
        kpt_list]
    return kpath_labels