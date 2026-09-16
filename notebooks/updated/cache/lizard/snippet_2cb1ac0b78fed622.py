def _reduce_name(cls, name, parse_dict):
    removal_indices = []
    for section, match in iteritems(parse_dict):
        try:
            matches = []
            if isinstance(match, dict) and 'compound_matches' in match:
                matches = match.get('compound_matches')
            elif not isinstance(match, list) and match is not None:
                matches = [match]
            for m in matches:
                valid_slice = True
                slice_a, slice_b = m.get('position')
                if removal_indices is []:
                    removal_indices.append((slice_a, slice_b))
                for r_slice_a, r_slice_b in removal_indices:
                    if slice_a == r_slice_a and slice_b == r_slice_b:
                        valid_slice = False
                    if (slice_a > r_slice_a or slice_a > r_slice_b or 
                        slice_b > r_slice_b or slice_b > r_slice_a):
                        slice_delta = r_slice_b - r_slice_a
                        slice_a -= slice_delta
                        slice_b -= slice_delta
                if valid_slice:
                    name = cls._string_remove_slice(name, slice_a, slice_b)
                    removal_indices.append((slice_a, slice_b))
        except (IndexError, TypeError):
            pass
    return name