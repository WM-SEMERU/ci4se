def _value_list_to_sciobj_dict(sciobj_value_list, lookup_list, lookup_dict,
    generate_dict):
    sciobj_dict = {}
    lookup_to_value_dict = {k: v for k, v in zip(lookup_list,
        sciobj_value_list)}
    for field_name, r_dict in lookup_dict.items():
        if r_dict['lookup_str'] in lookup_to_value_dict.keys():
            sciobj_dict[field_name] = lookup_to_value_dict[r_dict['lookup_str']
                ]
    for field_name, annotate_dict in generate_dict.items():
        for final_name, generate_func in annotate_dict['generate_dict'].items(
            ):
            sciobj_dict[field_name] = generate_func(lookup_to_value_dict)
    return sciobj_dict