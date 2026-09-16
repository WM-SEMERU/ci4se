def _prune(current, keys):
    pruned_current = {k: current[k] for k in keys if k in current}
    pruned_children = list(filter(None, [_prune(c, keys) for c in current.
        get('IORegistryEntryChildren', [])]))
    keep_current = any(k in current for k in keys) or pruned_children
    if keep_current:
        if pruned_children:
            pruned_current['IORegistryEntryChildren'] = pruned_children
        return pruned_current
    else:
        return {}