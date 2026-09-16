def emulate_network(network_constraints, roles=None, inventory_path=None,
    extra_vars=None):
    if not network_constraints:
        return
    if roles is None and inventory is None:
        raise ValueError("roles and inventory can't be None")
    if not extra_vars:
        extra_vars = {}
    logger.debug('Getting the ips of all nodes')
    tmpdir = os.path.join(os.getcwd(), TMP_DIRNAME)
    _check_tmpdir(tmpdir)
    utils_playbook = os.path.join(ANSIBLE_DIR, 'utils.yml')
    ips_file = os.path.join(tmpdir, 'ips.txt')
    options = {'enos_action': 'tc_ips', 'ips_file': ips_file}
    run_ansible([utils_playbook], roles=roles, extra_vars=options)
    logger.debug('Building all the constraints')
    constraints = _build_grp_constraints(roles, network_constraints)
    with open(ips_file) as f:
        ips = yaml.safe_load(f)
        ips_with_constraints = _build_ip_constraints(roles, ips, constraints)
        ips_with_constraints_file = os.path.join(tmpdir,
            'ips_with_constraints.yml')
        with open(ips_with_constraints_file, 'w') as g:
            yaml.dump(ips_with_constraints, g)
    logger.info('Enforcing the constraints')
    enable = network_constraints.setdefault('enable', True)
    utils_playbook = os.path.join(ANSIBLE_DIR, 'utils.yml')
    options = {'enos_action': 'tc_apply', 'ips_with_constraints':
        ips_with_constraints, 'tc_enable': enable}
    options.update(extra_vars)
    run_ansible([utils_playbook], roles=roles, inventory_path=
        inventory_path, extra_vars=options)