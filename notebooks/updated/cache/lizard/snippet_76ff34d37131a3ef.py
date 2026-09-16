def format_info(info_list):
    max_lengths = []
    if info_list:
        nr_columns = len(info_list[0])
    else:
        nr_columns = 0
    for i in range(nr_columns):
        max_lengths.append(max([len(info[i]) for info in info_list]))
    flattened_info_list = []
    for info_id in range(len(info_list)):
        info = info_list[info_id]
        for str_id in range(len(info) - 1):
            orig_str = info[str_id]
            indent = max_lengths[str_id] - len(orig_str)
            info[str_id] = orig_str + indent * b' '
        flattened_info_list.append(b' '.join(info) + b'\n')
    return flattened_info_list