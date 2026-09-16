def is_block(bin_list):
    id_set = set(my_bin[1] for my_bin in bin_list)
    start_id, end_id = min(id_set), max(id_set)
    return id_set == set(range(start_id, end_id + 1))