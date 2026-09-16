def get_dataset(catalog, identifier=None, title=None):
    msg = "Se requiere un 'identifier' o 'title' para buscar el dataset."
    assert identifier or title, msg
    catalog = read_catalog_obj(catalog)
    if identifier:
        try:
            return _get_dataset_by_identifier(catalog, identifier)
        except BaseException:
            try:
                catalog._build_index()
                return _get_dataset_by_identifier(catalog, identifier)
            except BaseException:
                filtered_datasets = get_datasets(catalog, {'dataset': {
                    'identifier': identifier}})
    elif title:
        filtered_datasets = get_datasets(catalog, {'dataset': {'title': title}}
            )
    if len(filtered_datasets) > 1:
        if identifier:
            raise ce.DatasetIdRepetitionError(identifier, filtered_datasets)
        elif title:
            raise ce.DatasetTitleRepetitionError(title, filtered_datasets)
    elif len(filtered_datasets) == 0:
        return None
    else:
        return filtered_datasets[0]