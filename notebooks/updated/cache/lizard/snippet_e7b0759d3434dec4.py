def from_config(cls, config):
    auth_key = None
    password_file = config['authentication.passwordFile']
    if password_file is not None:
        try:
            auth_key = open(config['authentication.passwordFile']).read()
            auth_key = re.sub('\\s', '', auth_key)
        except IOError:
            LOG.error('Could not load password file!')
            sys.exit(1)
    password = config['authentication.password']
    if password is not None:
        auth_key = password
    connector = Connector(mongo_address=config['mainAddress'], doc_managers
        =config['docManagers'], oplog_checkpoint=os.path.abspath(config[
        'oplogFile']), collection_dump=config['onlyDump'] or not config[
        'noDump'], only_dump=config['onlyDump'], batch_size=config[
        'batchSize'], continue_on_error=config['continueOnError'],
        auth_username=config['authentication.adminUsername'], auth_key=
        auth_key, fields=config['fields'], exclude_fields=config[
        'exclude_fields'], ns_set=config['namespaces.include'], ex_ns_set=
        config['namespaces.exclude'], dest_mapping=config[
        'namespaces.mapping'], namespace_options=config[
        'namespaces.namespace_options'], gridfs_set=config[
        'namespaces.gridfs'], ssl_certfile=config['ssl.sslCertfile'],
        ssl_keyfile=config['ssl.sslKeyfile'], ssl_ca_certs=config[
        'ssl.sslCACerts'], ssl_cert_reqs=config['ssl.sslCertificatePolicy'],
        tz_aware=config['timezoneAware'])
    return connector