def duplicate_object_hook(ordered_pairs):
    json_dict = {}
    for key, val in ordered_pairs:
        existing_val = json_dict.get(key)
        if not existing_val:
            json_dict[key] = val
        elif isinstance(existing_val, list):
            existing_val.append(val)
        else:
            json_dict[key] = [existing_val, val]
    return json_dict