def _calculate_matches_closures(groups):
    matches = []
    ns = sorted(groups.groups.keys())
    while ns:
        n = ns.pop(0)
        visited = [n]
        vs = [v for v in groups.get_group(n)['uuid_y']]
        while vs:
            v = vs.pop(0)
            if v in visited:
                continue
            nvs = [nv for nv in groups.get_group(v)['uuid_y']]
            vs += nvs
            visited.append(v)
            try:
                ns.remove(v)
            except:
                pass
        matches.append(visited)
    return matches