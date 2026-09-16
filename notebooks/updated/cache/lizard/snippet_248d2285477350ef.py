def adjust_events(events, labels=None, t_min=0.0, t_max=None, label_prefix='__'
    ):
    if t_min is not None:
        first_idx = np.argwhere(events >= t_min)
        if len(first_idx) > 0:
            if labels is not None:
                labels = labels[int(first_idx[0]):]
            events = events[int(first_idx[0]):]
        if events[0] > t_min:
            events = np.concatenate(([t_min], events))
            if labels is not None:
                labels.insert(0, '%sT_MIN' % label_prefix)
    if t_max is not None:
        last_idx = np.argwhere(events > t_max)
        if len(last_idx) > 0:
            if labels is not None:
                labels = labels[:int(last_idx[0])]
            events = events[:int(last_idx[0])]
        if events[-1] < t_max:
            events = np.concatenate((events, [t_max]))
            if labels is not None:
                labels.append('%sT_MAX' % label_prefix)
    return events, labels