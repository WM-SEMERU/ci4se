def _compare_suffix(self, other):
    if not self.suffix or not other.suffix:
        return True
    suffix_set = set(self.suffix_list + other.suffix_list)
    unique_suffixes = suffix_set & UNIQUE_SUFFIXES
    for key in EQUIVALENT_SUFFIXES:
        if key in unique_suffixes:
            unique_suffixes.remove(key)
            unique_suffixes.add(EQUIVALENT_SUFFIXES[key])
    return len(unique_suffixes) < 2