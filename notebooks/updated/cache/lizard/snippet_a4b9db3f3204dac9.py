def _wait_for_status(linode_id, status=None, timeout=300, quiet=True):
    if status is None:
        status = _get_status_id_by_name('brand_new')
    status_desc_waiting = _get_status_descr_by_id(status)
    interval = 5
    iterations = int(timeout / interval)
    for i in range(0, iterations):
        result = get_linode(kwargs={'linode_id': linode_id})
        if result['STATUS'] == status:
            return True
        status_desc_result = _get_status_descr_by_id(result['STATUS'])
        time.sleep(interval)
        log.log(logging.INFO if not quiet else logging.DEBUG,
            "Status for Linode %s is '%s', waiting for '%s'.", linode_id,
            status_desc_result, status_desc_waiting)
    return False