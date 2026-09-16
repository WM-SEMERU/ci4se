def update_network(cx_str, network_id, ndex_cred=None):
    server = 'http://public.ndexbio.org'
    username, password = get_default_ndex_cred(ndex_cred)
    nd = ndex2.client.Ndex2(server, username, password)
    try:
        logger.info('Getting network summary...')
        summary = nd.get_network_summary(network_id)
    except Exception as e:
        logger.error('Could not get NDEx network summary.')
        logger.error(e)
        return
    try:
        logger.info('Updating network...')
        cx_stream = io.BytesIO(cx_str.encode('utf-8'))
        nd.update_cx_network(cx_stream, network_id)
    except Exception as e:
        logger.error('Could not update NDEx network.')
        logger.error(e)
        return
    ver_str = summary.get('version')
    new_ver = _increment_ndex_ver(ver_str)
    profile = {'name': summary.get('name'), 'description': summary.get(
        'description'), 'version': new_ver}
    logger.info('Updating NDEx network (%s) profile to %s', network_id, profile
        )
    profile_retries = 5
    for _ in range(profile_retries):
        try:
            time.sleep(5)
            nd.update_network_profile(network_id, profile)
            break
        except Exception as e:
            logger.error('Could not update NDEx network profile.')
            logger.error(e)
    set_style(network_id, ndex_cred)