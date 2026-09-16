def _normalize_merge_diff(diff):
    new_diff = []
    for line in diff.splitlines():
        if line.strip():
            new_diff.append('+' + line)
    if new_diff:
        new_diff.insert(0,
            '! incremental-diff failed; falling back to echo of merge file')
    else:
        new_diff.append('! No changes specified in merge file.')
    return '\n'.join(new_diff)