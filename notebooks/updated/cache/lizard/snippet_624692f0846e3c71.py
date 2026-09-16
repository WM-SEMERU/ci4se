def check_empty_dict(GET_dict):
    empty = True
    for k, v in GET_dict.items():
        if v and k != 'p' and k != 'all':
            empty = False
    return empty