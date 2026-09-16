def _find_fuse_next(working_list, homology, tm):
    pattern = working_list[0]
    targets = working_list[1:]

    def graph_strands(strand1, strand2):
        graph = []
        for i, target in enumerate(targets):
            matchlen = homology_report(pattern, target, strand1, strand2,
                cutoff=homology, min_tm=tm)
            if matchlen:
                graph.append((i, matchlen, strand1, strand2))
        return graph
    graph_ww = graph_strands('w', 'w')
    graph_wc = graph_strands('w', 'c')
    graph_cw = graph_strands('c', 'w')
    graph_cc = graph_strands('c', 'c')
    graphs_w = graph_ww + graph_wc
    graphs_c = graph_cw + graph_cc
    graphs = graphs_w + graphs_c
    if len(graphs_w) > 1 or len(graphs_c) > 1:
        raise AmbiguousGibsonError('multiple compatible ends.')
    if len(graphs_w) == len(graphs_c) == 0:
        raise GibsonOverlapError('Failed to find compatible Gibson ends.')
    match = graphs[0]
    if match[2] == 'c':
        left_side = pattern.reverse_complement()
    else:
        left_side = pattern
    if match[3] == 'w':
        right_side = working_list.pop(match[0] + 1).reverse_complement()
    else:
        right_side = working_list.pop(match[0] + 1)
    working_list[0] = left_side + right_side[match[1]:]
    return working_list