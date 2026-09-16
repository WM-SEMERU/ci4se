def gen_bracket_mappings(docgraph, layer=None):
    if layer:
        namespace = dg.layer2namespace(layer)
    else:
        namespace = docgraph.ns
    pointing_chains = dg.get_pointing_chains(docgraph, layer=layer)
    markables = sorted(itertools.chain(*pointing_chains), key=dg.util.
        natural_sort_key)
    markable2chain = {}
    for chain in pointing_chains:
        chain_id = chain[0]
        for markable in chain:
            markable2chain[markable] = chain_id
    opening = defaultdict(list)
    closing = defaultdict(list)
    for markable in markables:
        if namespace + ':span' in docgraph.node[markable]:
            span_tokens = spanstring2tokens(docgraph, docgraph.node[
                markable][namespace + ':span'])
            opening[span_tokens[0]].append(markable)
            closing[span_tokens[-1]].append(markable)
    return opening, closing, markable2chain