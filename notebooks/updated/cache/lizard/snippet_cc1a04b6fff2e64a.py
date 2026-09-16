def remove_dupes(list_with_dupes):
    visited = set()
    visited_add = visited.add
    out = [entry for entry in list_with_dupes if not (entry in visited or
        visited_add(entry))]
    return out