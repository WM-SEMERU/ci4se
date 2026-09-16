def find_missing_projections(label_list, projections):
    unmapped_combinations = set()
    if WILDCARD_COMBINATION in projections:
        return []
    for labeled_segment in label_list.ranges():
        combination = tuple(sorted([label.value for label in
            labeled_segment[2]]))
        if combination not in projections:
            unmapped_combinations.add(combination)
    return sorted(unmapped_combinations)