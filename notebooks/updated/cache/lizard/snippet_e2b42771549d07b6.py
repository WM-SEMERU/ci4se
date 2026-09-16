def cluster_ensembles(cluster_runs, hdf5_file_name=None, verbose=False,
    N_clusters_max=None):
    if hdf5_file_name is None:
        hdf5_file_name = './Cluster_Ensembles.h5'
    fileh = tables.open_file(hdf5_file_name, 'w')
    fileh.create_group(fileh.root, 'consensus_group')
    fileh.close()
    cluster_ensemble = []
    score = np.empty(0)
    if cluster_runs.shape[1] > 10000:
        consensus_functions = [HGPA, MCLA]
        function_names = ['HGPA', 'MCLA']
        print(
            """
INFO: Cluster_Ensembles: cluster_ensembles: due to a rather large number of cells in your data-set, using only 'HyperGraph Partitioning Algorithm' (HGPA) and 'Meta-CLustering Algorithm' (MCLA) as ensemble consensus functions.
"""
            )
    else:
        consensus_functions = [CSPA, HGPA, MCLA]
        function_names = ['CSPA', 'HGPA', 'MCLA']
    hypergraph_adjacency = build_hypergraph_adjacency(cluster_runs)
    store_hypergraph_adjacency(hypergraph_adjacency, hdf5_file_name)
    for i in range(len(consensus_functions)):
        cluster_ensemble.append(consensus_functions[i](hdf5_file_name,
            cluster_runs, verbose, N_clusters_max))
        score = np.append(score, ceEvalMutual(cluster_runs,
            cluster_ensemble[i], verbose))
        print('\nINFO: Cluster_Ensembles: cluster_ensembles: {0} at {1}.'.
            format(function_names[i], score[i]))
        print('*****')
    return cluster_ensemble[np.argmax(score)]