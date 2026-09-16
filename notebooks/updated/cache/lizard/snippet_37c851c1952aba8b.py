def rich_club_wd(CIJ, klevel=None):
    nr_nodes = len(CIJ)
    deg = np.sum(CIJ != 0, axis=0) + np.sum(CIJ.T != 0, axis=0)
    if klevel is None:
        klevel = np.max(deg)
    Rw = np.zeros((klevel,))
    wrank = np.sort(CIJ.flat)[::-1]
    for k in range(klevel):
        SmallNodes, = np.where(deg < k + 1)
        if np.size(SmallNodes) == 0:
            Rw[k] = np.nan
            continue
        cutCIJ = np.delete(np.delete(CIJ, SmallNodes, axis=0), SmallNodes,
            axis=1)
        Wr = np.sum(cutCIJ)
        Er = np.size(np.where(cutCIJ.flat != 0), axis=1)
        wrank_r = wrank[:Er]
        Rw[k] = Wr / np.sum(wrank_r)
    return Rw