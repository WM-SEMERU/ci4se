def _collapse_address_list_recursive(addresses):
    ret_array = []
    optimized = False
    for cur_addr in addresses:
        if not ret_array:
            ret_array.append(cur_addr)
            continue
        if cur_addr in ret_array[-1]:
            optimized = True
        elif cur_addr == ret_array[-1].supernet().subnet()[1]:
            ret_array.append(ret_array.pop().supernet())
            optimized = True
        else:
            ret_array.append(cur_addr)
    if optimized:
        return _collapse_address_list_recursive(ret_array)
    return ret_array