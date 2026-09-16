def get_possible_importers(file_uris, current_doc=None):
    importers = []
    for importer in IMPORTERS:
        if importer.can_import(file_uris, current_doc):
            importers.append(importer)
    return importers