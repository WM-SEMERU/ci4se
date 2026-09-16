def createCatalog(config, roi=None, lon=None, lat=None):
    import ugali.observation.catalog
    if roi is None:
        roi = createROI(config, lon, lat)
    catalog = ugali.observation.catalog.Catalog(config, roi=roi)
    return catalog