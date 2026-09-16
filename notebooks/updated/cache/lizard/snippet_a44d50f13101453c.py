def wait_ssh(roles, retries=100, interval=30):
    utils_playbook = os.path.join(ANSIBLE_DIR, 'utils.yml')
    options = {'enos_action': 'ping'}
    for i in range(0, retries):
        try:
            run_ansible([utils_playbook], roles=roles, extra_vars=options,
                on_error_continue=False)
            break
        except EnosUnreachableHostsError as e:
            logger.info('Hosts unreachable: %s ' % e.hosts)
            logger.info('Retrying... %s/%s' % (i + 1, retries))
            time.sleep(interval)
    else:
        raise EnosSSHNotReady('Maximum retries reached')