def sid(tnet, communities, axis=0, calc='global', decay=0):
    r
    tnet, netinfo = utils.process_input(tnet, ['C', 'G', 'TN'])
    D = temporal_degree_centrality(tnet, calc='time', communities=
        communities, decay=decay)
    network_ids = np.unique(communities)
    communities_size = np.array([sum(communities == n) for n in network_ids])
    sid = np.zeros([network_ids.max() + 1, network_ids.max() + 1, tnet.
        shape[-1]])
    for n in network_ids:
        for m in network_ids:
            betweenmodulescaling = 1 / (communities_size[n] *
                communities_size[m])
            if netinfo['nettype'][1] == 'd':
                withinmodulescaling = 1 / (communities_size[n] *
                    communities_size[n])
            elif netinfo['nettype'][1] == 'u':
                withinmodulescaling = 2 / (communities_size[n] * (
                    communities_size[n] - 1))
                if n == m:
                    betweenmodulescaling = withinmodulescaling
            sid[(n), (m), :] = withinmodulescaling * D[(n), (n), :
                ] - betweenmodulescaling * D[(n), (m), :]
    sid[np.isnan(sid)] = 0
    if calc == 'global':
        return np.sum(np.sum(sid, axis=1), axis=0)
    elif calc == 'communities_avg':
        return np.sum(sid, axis=axis)
    else:
        return sid