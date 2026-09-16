def submit_and_verify(xml_str=None, xml_file=None, xml_root=None, config=
    None, session=None, dry_run=None, **kwargs):
    try:
        config = config or configuration.get_config()
        xml_root = _get_xml_root(xml_root, xml_str, xml_file)
        submit_config = SubmitConfig(xml_root, config, **kwargs)
        session = session or utils.get_session(submit_config.credentials,
            config)
        submit_response = submit(xml_root, submit_config, session, dry_run=
            dry_run, **kwargs)
    except Dump2PolarionException as err:
        logger.error(err)
        return None
    valid_response = submit_response.validate_response()
    if not valid_response or kwargs.get('no_verify'):
        return submit_response.response
    response = verify_submit(session, submit_config.queue_url,
        submit_config.log_url, submit_response.job_ids, timeout=kwargs.get(
        'verify_timeout'), log_file=kwargs.get('log_file'))
    return response