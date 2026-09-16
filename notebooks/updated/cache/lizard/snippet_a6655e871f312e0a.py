def flatten_group(group_to_flatten, root, recursive=True, group_filter=lambda
    x: True, path_filter=lambda x: True, path_conversions=CONVERSIONS,
    group_search_xpath=SVG_GROUP_TAG):
    if not any(group_to_flatten is descendant for descendant in root.iter()):
        warnings.warn(
            'The requested group_to_flatten is not a descendant of root')
        return []
    desired_groups = set()
    if recursive:
        for group in group_to_flatten.iter():
            desired_groups.add(id(group))
    else:
        desired_groups.add(id(group_to_flatten))

    def desired_group_filter(x):
        return id(x) in desired_groups and group_filter(x)
    return flatten_all_paths(root, desired_group_filter, path_filter,
        path_conversions, group_search_xpath)