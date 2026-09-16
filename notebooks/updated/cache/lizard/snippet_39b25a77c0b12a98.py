def make_node_dict(outer_list, sort='zone'):
    raw_dict = {}
    x = 1
    for inner_list in outer_list:
        for node in inner_list:
            raw_dict[x] = node
            x += 1
    if sort == 'name':
        srt_dict = OrderedDict(sorted(raw_dict.items(), key=lambda k: (k[1]
            .cloud, k[1].name.lower())))
    else:
        srt_dict = OrderedDict(sorted(raw_dict.items(), key=lambda k: (k[1]
            .cloud, k[1].zone, k[1].name.lower())))
    x = 1
    node_dict = {}
    for i, v in srt_dict.items():
        node_dict[x] = v
        x += 1
    return node_dict