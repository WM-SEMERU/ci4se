def to_dict(for_lists, global_vars, data_dict):
    res = {}
    for a in global_vars:
        a_list = a.split('.')
        tmp = res
        for i in a_list[:-1]:
            if not i in tmp:
                tmp[i] = {}
            tmp = tmp[i]
        tmp[a_list[-1]] = reduce(getattr, a_list[1:], data_dict[a_list[0]])
    for for_list in for_lists:
        it = for_list.name.split('.')
        tmp = res
        for i in it[:-1]:
            if not i in tmp:
                tmp[i] = {}
            tmp = tmp[i]
        if not it[-1] in tmp:
            tmp[it[-1]] = []
        tmp = tmp[it[-1]]
        if not it[0] in data_dict:
            continue
        if len(it) == 1:
            loop = enumerate(data_dict[it[0]])
        else:
            loop = enumerate(reduce(getattr, it[-1:], data_dict[it[0]]))
        for i, val in loop:
            new_data_dict = {for_list.var_from: val}
            if len(tmp) <= i:
                tmp.append({})
            tmp[i] = ForList.__recur_to_dict(for_list, new_data_dict, tmp[i])
    return res