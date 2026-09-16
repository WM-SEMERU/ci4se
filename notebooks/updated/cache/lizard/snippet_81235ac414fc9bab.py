def net_graph(block=None, split_state=False):
    block = working_block(block)
    from .wire import Register
    graph = {}
    for net in block.logic:
        graph[net] = {}
    wire_src_dict, wire_dst_dict = block.net_connections()
    dest_set = set(wire_src_dict.keys())
    arg_set = set(wire_dst_dict.keys())
    dangle_set = dest_set.symmetric_difference(arg_set)
    for w in dangle_set:
        graph[w] = {}
    if split_state:
        for w in block.wirevector_subset(Register):
            graph[w] = {}
    for w in (dest_set & arg_set):
        try:
            _from = wire_src_dict[w]
        except Exception:
            _from = w
        if split_state and isinstance(w, Register):
            _from = w
        try:
            _to_list = wire_dst_dict[w]
        except Exception:
            _to_list = [w]
        for _to in _to_list:
            graph[_from][_to] = w
    return graph