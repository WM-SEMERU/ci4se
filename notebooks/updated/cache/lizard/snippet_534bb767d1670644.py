def nmf_kfold(data, k, n_runs=10, **nmf_params):
    nmf = NMF(k)
    W_list = []
    kf = KFold(n_splits=n_runs, shuffle=True)
    for train_index, test_index in kf.split(data.T):
        W = nmf.fit_transform(data[:, (train_index)])
        W_list.append(W)
    W_stacked = np.hstack(W_list)
    nmf_w = nmf.fit_transform(W_stacked)
    nmf_h = nmf.components_
    H_new = data.T.dot(nmf_w).T
    nmf2 = NMF(k, init='custom')
    nmf_w = nmf2.fit_transform(data, W=nmf_w, H=H_new)
    H_new = nmf2.components_
    return nmf_w, H_new