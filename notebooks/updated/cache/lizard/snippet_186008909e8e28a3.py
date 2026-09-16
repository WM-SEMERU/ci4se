def _get_dataset_index(catalog, dataset_identifier, dataset_title, logger=None
    ):
    logger = logger or pydj_logger
    matching_datasets = []
    for idx, dataset in enumerate(catalog['catalog_dataset']):
        if dataset['dataset_identifier'] == dataset_identifier:
            if dataset['dataset_title'] == dataset_title:
                matching_datasets.append(idx)
            else:
                logger.warning(ce.DatasetUnexpectedTitle(dataset_identifier,
                    dataset['dataset_title'], dataset_title))
    no_dsets_msg = 'No hay ningun dataset con el identifier {}'.format(
        dataset_identifier)
    many_dsets_msg = 'Hay mas de un dataset con el identifier {}: {}'.format(
        dataset_identifier, matching_datasets)
    if len(matching_datasets) == 0:
        logger.error(no_dsets_msg)
        return None
    elif len(matching_datasets) > 1:
        logger.error(many_dsets_msg)
        return None
    else:
        return matching_datasets[0]