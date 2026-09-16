def read_ckan_catalog(portal_url):
    portal = RemoteCKAN(portal_url)
    try:
        status = portal.call_action('status_show', requests_kwargs={
            'verify': False})
        packages_list = portal.call_action('package_list', requests_kwargs=
            {'verify': False})
        groups_list = portal.call_action('group_list', requests_kwargs={
            'verify': False})
        packages = []
        num_packages = len(packages_list)
        for index, pkg in enumerate(packages_list):
            msg = 'Leyendo dataset {} de {}'.format(index + 1, num_packages)
            logger.info(msg)
            packages.append(portal.call_action('package_show', {'id': pkg},
                requests_kwargs={'verify': False}))
            time.sleep(0.2)
        groups = [portal.call_action('group_show', {'id': grp},
            requests_kwargs={'verify': False}) for grp in groups_list]
        catalog = map_status_to_catalog(status)
        catalog['dataset'] = map_packages_to_datasets(packages, portal_url)
        catalog['themeTaxonomy'] = map_groups_to_themes(groups)
    except (CKANAPIError, RequestException) as e:
        logger.exception('Error al procesar el portal %s', portal_url,
            exc_info=True)
        raise NonParseableCatalog(portal_url, e)
    return catalog