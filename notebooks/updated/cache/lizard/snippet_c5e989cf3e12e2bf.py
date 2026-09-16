def _find_by_name(tree_data, name, is_dir, start_at):
    try:
        item = tree_data[start_at]
        if item and item[2] == name and S_ISDIR(item[1]) == is_dir:
            tree_data[start_at] = None
            return item
    except IndexError:
        pass
    for index, item in enumerate(tree_data):
        if item and item[2] == name and S_ISDIR(item[1]) == is_dir:
            tree_data[index] = None
            return item
    return None