def add_firewalld_port(port, permanent=True):
    yum_install(packages=['firewalld'])
    log_green('adding a new fw rule: %s' % port)
    with settings(hide('warnings', 'running', 'stdout', 'stderr'),
        warn_only=True, capture=True):
        p = ''
        if permanent:
            p = '--permanent'
        sudo('firewall-cmd --add-port %s %s' % (port, p))
        sudo('systemctl restart firewalld')