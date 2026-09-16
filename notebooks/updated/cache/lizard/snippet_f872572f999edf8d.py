def node_to_mfd(node, taglist):
    if 'incrementalMFD' in taglist:
        mfd = node_to_evenly_discretized(node.nodes[taglist.index(
            'incrementalMFD')])
    elif 'truncGutenbergRichterMFD' in taglist:
        mfd = node_to_truncated_gr(node.nodes[taglist.index(
            'truncGutenbergRichterMFD')])
    else:
        mfd = None
    return mfd