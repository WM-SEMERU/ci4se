def merge_labeled_intervals(x_intervals, x_labels, y_intervals, y_labels):
    r
    align_check = [x_intervals[0, 0] == y_intervals[0, 0], x_intervals[-1, 
        1] == y_intervals[-1, 1]]
    if False in align_check:
        raise ValueError(
            "Time intervals do not align; did you mean to call 'adjust_intervals()' first?"
            )
    time_boundaries = np.unique(np.concatenate([x_intervals, y_intervals],
        axis=0))
    output_intervals = np.array([time_boundaries[:-1], time_boundaries[1:]]).T
    x_labels_out, y_labels_out = [], []
    x_label_range = np.arange(len(x_labels))
    y_label_range = np.arange(len(y_labels))
    for t0, _ in output_intervals:
        x_idx = x_label_range[t0 >= x_intervals[:, (0)]]
        x_labels_out.append(x_labels[x_idx[-1]])
        y_idx = y_label_range[t0 >= y_intervals[:, (0)]]
        y_labels_out.append(y_labels[y_idx[-1]])
    return output_intervals, x_labels_out, y_labels_out