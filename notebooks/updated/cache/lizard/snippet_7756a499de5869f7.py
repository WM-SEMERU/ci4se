def wrap_star_digger(item, type_str, data_name='Value'):
    ret = []
    if type(item) == dict:
        if 'Type' in item and item['Type'] == type_str and data_name in item:
            if len(item[data_name]) > 1:
                pass
            return item[data_name]
        else:
            for k in item:
                sub_ret = wrap_star_digger(item[k], type_str, data_name)
                if sub_ret:
                    ret.extend(sub_ret)
    elif type(item) == list:
        for i in item:
            sub_ret = wrap_star_digger(i, type_str, data_name)
            if sub_ret:
                ret.extend(sub_ret)
    return ret