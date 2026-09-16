def get_kmgraph_meta(mapper_summary):
    d = mapper_summary['custom_meta']
    meta = '<b>N_cubes:</b> ' + str(d['n_cubes']
        ) + ' <b>Perc_overlap:</b> ' + str(d['perc_overlap'])
    meta += '<br><b>Nodes:</b> ' + str(mapper_summary['n_nodes']
        ) + ' <b>Edges:</b> ' + str(mapper_summary['n_edges']
        ) + ' <b>Total samples:</b> ' + str(mapper_summary['n_total']
        ) + ' <b>Unique_samples:</b> ' + str(mapper_summary['n_unique'])
    return meta