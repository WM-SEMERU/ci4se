def compute_group_overlap_score(ref_labels, pred_labels,
    threshold_overlap_pred=0.5, threshold_overlap_ref=0.5):
    ref_unique, ref_counts = np.unique(ref_labels, return_counts=True)
    ref_dict = dict(zip(ref_unique, ref_counts))
    pred_unique, pred_counts = np.unique(pred_labels, return_counts=True)
    pred_dict = dict(zip(pred_unique, pred_counts))
    summary = []
    for true in ref_unique:
        sub_pred_unique, sub_pred_counts = np.unique(pred_labels[true ==
            ref_labels], return_counts=True)
        relative_overlaps_pred = [(sub_pred_counts[i] / pred_dict[n]) for i,
            n in enumerate(sub_pred_unique)]
        relative_overlaps_ref = [(sub_pred_counts[i] / ref_dict[true]) for 
            i, n in enumerate(sub_pred_unique)]
        pred_best_index = np.argmax(relative_overlaps_pred)
        summary.append(1 if relative_overlaps_pred[pred_best_index] >=
            threshold_overlap_pred and relative_overlaps_ref[
            pred_best_index] >= threshold_overlap_ref else 0)
    return sum(summary) / len(summary)