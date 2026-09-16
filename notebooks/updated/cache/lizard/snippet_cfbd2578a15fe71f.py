def diff_sevice_by_text(service_name, service, environment, cf_client,
    repo_root):
    global ret_code
    logger.info('Investigating textual diff for `%s`:`%s` in environment `%s`',
        service['type'], service_name, environment)
    try:
        local_template = render_local_template(service_name, environment,
            repo_root, service['template_file'])
        current_template = fetch_current_cloudformation_template(service_name,
            environment, cf_client)
    except Exception as e:
        ret_code = 2
        logger.error(e)
        return
    ret = diff_string_templates(local_template, current_template)
    if not ret:
        logger.info(
            'Deployed service `%s` in environment `%s` matches the local template.'
            , service_name, environment)
    else:
        ret_code = 1
        logger.error(
            'Service `%s` in environment `%s` differs from the local template.'
            , service_name, environment)
        logger.info("""Change details:
        %s""", indentify(ret))