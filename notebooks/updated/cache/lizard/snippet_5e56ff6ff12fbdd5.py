def _comparison_generator(old_list, new_list, compare_fn):
    old_index = 0
    new_index = 0
    while old_index < len(old_list) and new_index < len(new_list):
        old_value = old_list[old_index]
        new_value = new_list[new_index]
        status = compare_fn(old_value, new_value)
        if status == 0:
            yield old_value, new_value
            old_index += 1
            new_index += 1
        elif status == -1:
            yield old_value, None
            old_index += 1
        else:
            yield None, new_value
            new_index += 1
    while old_index < len(old_list):
        yield old_list[old_index], None
        old_index += 1
    while new_index < len(new_list):
        yield None, new_list[new_index]
        new_index += 1