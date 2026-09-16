def create_job(name=None, config_xml=None, saltenv='base'):
    if not name:
        raise SaltInvocationError("Required parameter 'name' is missing")
    if job_exists(name):
        raise CommandExecutionError("Job '{0}' already exists".format(name))
    if not config_xml:
        config_xml = jenkins.EMPTY_CONFIG_XML
    else:
        config_xml_file = _retrieve_config_xml(config_xml, saltenv)
        with salt.utils.files.fopen(config_xml_file) as _fp:
            config_xml = salt.utils.stringutils.to_unicode(_fp.read())
    server = _connect()
    try:
        server.create_job(name, config_xml)
    except jenkins.JenkinsException as err:
        raise CommandExecutionError("Encountered error creating job '{0}': {1}"
            .format(name, err))
    return config_xml