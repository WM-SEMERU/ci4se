def _CheckConditionsShortCircuit(content_conditions, pathspec):
    matches = []
    for cond in content_conditions:
        with vfs.VFSOpen(pathspec) as vfs_file:
            cur_matches = list(cond.Search(vfs_file))
        if cur_matches:
            matches.extend(cur_matches)
        else:
            return []
    return matches