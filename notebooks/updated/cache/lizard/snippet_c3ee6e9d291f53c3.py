def read_line(csv_contents, options, prop_indices, mol):
    status_field = options.status_field
    active_label = options.active_label
    decoy_label = options.decoy_label
    active_value_matcher = re.compile(active_label)
    decoy_value_matcher = re.compile(decoy_label)
    status_label_index = prop_indices[status_field]
    if not active_value_matcher.match(csv_contents[status_label_index]
        ) and not decoy_value_matcher.match(csv_contents[status_label_index]):
        print('\n molecule lacks appropriate status label')
        return 1
    for prop_label in prop_indices.keys():
        value_index = prop_indices[prop_label]
        prop_value = csv_contents[value_index]
        mol.SetProp(prop_label, prop_value)
    return mol