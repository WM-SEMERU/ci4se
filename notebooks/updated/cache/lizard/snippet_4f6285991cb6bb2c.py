def fake_lens_path_set(lens_path, value, obj):
    segment = head(lens_path)
    obj_copy = copy.copy(obj)

    def set_array_index(i, v, l):
        try:
            l[i] = v
        except IndexError:
            for _ in range(i - len(l) + 1):
                l.append(None)
            l[i] = v
    if not length(lens_path) - 1:
        new_value = value
    else:
        found_or_created = item_path_or(if_else(lambda segment: segment.
            isnumeric(), always([]), always({}))(head(tail(lens_path))),
            segment, obj)
        new_value = fake_lens_path_set(tail(lens_path), value, found_or_created
            )
    if segment.isnumeric():
        set_array_index(int(segment), new_value, obj_copy)
    else:
        obj_copy[segment] = new_value
    return obj_copy