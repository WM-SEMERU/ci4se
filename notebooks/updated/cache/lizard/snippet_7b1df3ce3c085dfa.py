def wait_for_compute_zone_operation(compute, project_name, operation, zone):
    logger.info(
        'wait_for_compute_zone_operation: Waiting for operation {} to finish...'
        .format(operation['name']))
    for _ in range(MAX_POLLS):
        result = compute.zoneOperations().get(project=project_name,
            operation=operation['name'], zone=zone).execute()
        if 'error' in result:
            raise Exception(result['error'])
        if result['status'] == 'DONE':
            logger.info(
                'wait_for_compute_zone_operation: Operation {} finished.'.
                format(operation['name']))
            break
        time.sleep(POLL_INTERVAL)
    return result