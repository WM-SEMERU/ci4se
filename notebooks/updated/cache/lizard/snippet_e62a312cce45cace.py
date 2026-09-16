def arcsin_sqrt(biom_tbl):
    arcsint = lambda data, id_, md: np.arcsin(np.sqrt(data))
    tbl_relabd = relative_abd(biom_tbl)
    tbl_asin = tbl_relabd.transform(arcsint, inplace=False)
    return tbl_asin