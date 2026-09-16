def finish_init(environment, start_web, create_sysadmin, log_syslog=False,
    do_install=True, quiet=False, site_url=None, interactive=False, init_db
    =True):
    if not init_db:
        start_web = False
        create_sysadmin = False
    if do_install:
        install_all(environment, False, verbose=False, quiet=quiet)
    if init_db:
        if not quiet:
            write('Initializing database')
        environment.install_postgis_sql()
        environment.ckan_db_init()
    if not quiet:
        write('\n')
    if site_url:
        try:
            site_url = site_url.format(address=environment.address, port=
                environment.port)
            environment.site_url = site_url
            environment.save_site(False)
        except (KeyError, IndexError, ValueError) as e:
            raise DatacatsError('Could not parse site_url: {}'.format(e))
    if start_web:
        environment.start_ckan(log_syslog=log_syslog)
        if not quiet and not interactive:
            write('Starting web server at {0} ...\n'.format(environment.
                web_address()))
    if create_sysadmin:
        try:
            adminpw = confirm_password()
            environment.create_admin_set_password(adminpw)
        except KeyboardInterrupt:
            print
    if not start_web:
        environment.stop_supporting_containers()