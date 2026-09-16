def raise_on_major_version_mismatch(work_request, local_version):
    request_major_version = get_major_version(work_request.version)
    local_major_version = get_major_version(local_version)
    if request_major_version != local_major_version:
        raise ValueError('Received major version mismatch. request:{} local:{}'
            .format(work_request.version, local_version))
    else:
        logging.info('Ignoring non-major version mismatch request:{} local:{}'
            .format(work_request.version, local_version))