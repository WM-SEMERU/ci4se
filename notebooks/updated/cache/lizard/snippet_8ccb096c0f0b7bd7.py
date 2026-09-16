def dist_mat_km(catalog):
    dist_mat = np.array([np.array([0.0] * len(catalog))] * len(catalog))
    for i, master in enumerate(catalog):
        mast_list = []
        if master.preferred_origin():
            master_ori = master.preferred_origin()
        else:
            master_ori = master.origins[-1]
        master_tup = (master_ori.latitude, master_ori.longitude, master_ori
            .depth // 1000)
        for slave in catalog:
            if slave.preferred_origin():
                slave_ori = slave.preferred_origin()
            else:
                slave_ori = slave.origins[-1]
            slave_tup = (slave_ori.latitude, slave_ori.longitude, slave_ori
                .depth // 1000)
            mast_list.append(dist_calc(master_tup, slave_tup))
        for j in range(i, len(catalog)):
            dist_mat[i, j] = mast_list[j]
    for i in range(1, len(catalog)):
        for j in range(i):
            dist_mat[i, j] = dist_mat.T[i, j]
    return dist_mat