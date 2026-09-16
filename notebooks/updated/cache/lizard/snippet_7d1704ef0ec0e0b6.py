def normalize_layout(layout, min_percentile=1, max_percentile=99,
    relative_margin=0.1):
    mins = np.percentile(layout, min_percentile, axis=0)
    maxs = np.percentile(layout, max_percentile, axis=0)
    mins -= relative_margin * (maxs - mins)
    maxs += relative_margin * (maxs - mins)
    clipped = np.clip(layout, mins, maxs)
    clipped -= clipped.min(axis=0)
    clipped /= clipped.max(axis=0)
    return clipped