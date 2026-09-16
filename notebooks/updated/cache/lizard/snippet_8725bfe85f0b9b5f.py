def get_check_and_report(client_site_url, apikey, get_resource_ids_to_check,
    get_url_for_id, check_url, upsert_result):
    logger = _get_logger()
    resource_ids = get_resource_ids_to_check(client_site_url, apikey)
    for resource_id in resource_ids:
        try:
            url = get_url_for_id(client_site_url, apikey, resource_id)
        except CouldNotGetURLError:
            logger.info(
                'This link checker was not authorized to access resource {0}, skipping.'
                .format(resource_id))
            continue
        result = check_url(url)
        status = result['status']
        reason = result['reason']
        if result['alive']:
            logger.info(
                'Checking URL {0} of resource {1} succeeded with status {2}:'
                .format(url, resource_id, status))
        else:
            logger.info(
                'Checking URL {0} of resource {1} failed with error {2}:'.
                format(url, resource_id, reason))
        upsert_result(client_site_url, apikey, resource_id=resource_id,
            result=result)