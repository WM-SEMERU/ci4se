def duplicates_removed(it, already_seen=()):
    lst = []
    seen = set()
    for i in it:
        if i in seen or i in already_seen:
            continue
        lst.append(i)
        seen.add(i)
    return lst