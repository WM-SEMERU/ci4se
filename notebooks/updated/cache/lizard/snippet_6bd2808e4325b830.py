def merge_range_pairs(prs):
    new_prs = []
    sprs = [sorted(p) for p in prs]
    sprs = sorted(sprs)
    merged = False
    x = 0
    while x < len(sprs):
        newx = x + 1
        new_pair = list(sprs[x])
        for y in range(x + 1, len(sprs)):
            if new_pair[0] <= sprs[y][0] - 1 <= new_pair[1]:
                new_pair[0] = min(new_pair[0], sprs[y][0])
                new_pair[1] = max(new_pair[1], sprs[y][1])
                newx = y + 1
        if new_pair not in new_prs:
            new_prs.append(new_pair)
        x = newx
    return new_prs