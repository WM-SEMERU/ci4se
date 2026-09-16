def make_catalog_sources(catalog_roi_model, source_names):
    sources = {}
    for source_name in source_names:
        sources[source_name] = catalog_roi_model[source_name]
    return sources