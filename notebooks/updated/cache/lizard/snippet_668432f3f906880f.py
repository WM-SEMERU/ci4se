def sample_dimension(trajs, dimension, n_frames, scheme='linear'):
    fixed_indices = list(trajs.keys())
    trajs = [trajs[k][:, ([dimension])] for k in fixed_indices]
    txx = np.concatenate([traj[:, (0)] for traj in trajs])
    if scheme == 'linear':
        spaced_points = np.linspace(np.min(txx), np.max(txx), n_frames)
        spaced_points = spaced_points[:, (np.newaxis)]
    elif scheme == 'random':
        spaced_points = np.sort(np.random.choice(txx, n_frames))
        spaced_points = spaced_points[:, (np.newaxis)]
    elif scheme == 'edge':
        _cut_point = n_frames // 2
        txx = np.sort(txx)
        spaced_points = np.hstack((txx[:_cut_point], txx[-_cut_point:]))
        spaced_points = np.reshape(spaced_points, newshape=(len(
            spaced_points), 1))
    else:
        raise ValueError('Scheme has be to one of linear, random or edge')
    tree = KDTree(trajs)
    dists, inds = tree.query(spaced_points)
    return [(fixed_indices[i], j) for i, j in inds]