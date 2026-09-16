def _update_with_replacement(lhs_dict, rhs_dict):
    combined_dict = itertools.chain(lhs_dict.items(), rhs_dict.items())
    string_map = {key.as_string(): (key, value) for key, value in combined_dict
        }
    return dict(string_map.values())