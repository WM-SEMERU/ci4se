def _rm_similarlags(stations, nodes, lags, threshold):
    netdif = abs((lags.T - lags.T[0]).sum(axis=1).reshape(1, len(nodes))
        ) > threshold
    for i in range(len(nodes)):
        _netdif = abs((lags.T - lags.T[i]).sum(axis=1).reshape(1, len(nodes))
            ) > threshold
        netdif = np.concatenate((netdif, _netdif), axis=0)
        sys.stdout.write('\r' + str(float(i) // len(nodes) * 100) + '% \r')
        sys.stdout.flush()
    nodes_out = [nodes[0]]
    node_indices = [0]
    print('\n')
    print(len(nodes))
    for i in range(1, len(nodes)):
        if np.all(netdif[i][node_indices]):
            node_indices.append(i)
            nodes_out.append(nodes[i])
    lags_out = lags.T[node_indices].T
    print('Removed ' + str(len(nodes) - len(nodes_out)) + ' duplicate nodes')
    return stations, nodes_out, lags_out