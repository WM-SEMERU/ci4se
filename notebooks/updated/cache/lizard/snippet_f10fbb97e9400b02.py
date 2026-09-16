def add_chain_info(data_api, data_setters, chain_index):
    chain_id = data_api.chain_id_list[chain_index]
    chain_name = data_api.chain_name_list[chain_index]
    num_groups = data_api.groups_per_chain[chain_index]
    data_setters.set_chain_info(chain_id, chain_name, num_groups)
    next_ind = data_api.group_counter + num_groups
    last_ind = data_api.group_counter
    for group_ind in range(last_ind, next_ind):
        add_group(data_api, data_setters, group_ind)
        data_api.group_counter += 1
    data_api.chain_counter += 1