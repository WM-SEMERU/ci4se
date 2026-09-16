def mergeCatalogs(catalog_list):
    for c in catalog_list:
        if c.data.dtype.names != catalog_list[0].data.dtype.names:
            msg = 'Catalog data columns not the same.'
            raise Exception(msg)
    data = np.concatenate([c.data for c in catalog_list])
    config = catalog_list[0].config
    return Catalog(config, data=data)