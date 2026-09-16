def jpath_values(structure, jpath):
    nodes_a = [structure]
    nodes_b = []
    chunks = jpath_parse_c(jpath)
    for chnk in chunks:
        for node in nodes_a:
            key = chnk['n']
            if not isinstance(node, dict) and not isinstance(node,
                collections.Mapping):
                continue
            if 'i' in chnk:
                idx = chnk['i']
                if not key in node or not isinstance(node[key], (list,
                    collections.MutableSequence)) or not node[key]:
                    continue
                try:
                    if str(idx) == '*':
                        nodes_b.extend(node[key])
                    else:
                        nodes_b.append(node[key][idx])
                except:
                    pass
            else:
                if not key in node:
                    continue
                if isinstance(node[key], (list, collections.MutableSequence)):
                    for i in node[key]:
                        nodes_b.append(i)
                else:
                    nodes_b.append(node[key])
        nodes_a = nodes_b
        nodes_b = []
    return nodes_a