def _apply_dvportgroup_config(pg_name, pg_spec, pg_conf):
    log.trace("Building portgroup's '%s' spec", pg_name)
    if 'name' in pg_conf:
        pg_spec.name = pg_conf['name']
    if 'description' in pg_conf:
        pg_spec.description = pg_conf['description']
    if 'num_ports' in pg_conf:
        pg_spec.numPorts = pg_conf['num_ports']
    if 'type' in pg_conf:
        pg_spec.type = pg_conf['type']
    if not pg_spec.defaultPortConfig:
        for prop in ['vlan_id', 'out_shaping', 'security_policy', 'teaming']:
            if prop in pg_conf:
                pg_spec.defaultPortConfig = vim.VMwareDVSPortSetting()
    if 'vlan_id' in pg_conf:
        pg_spec.defaultPortConfig.vlan = (vim.
            VmwareDistributedVirtualSwitchVlanIdSpec())
        pg_spec.defaultPortConfig.vlan.vlanId = pg_conf['vlan_id']
    if 'out_shaping' in pg_conf:
        if not pg_spec.defaultPortConfig.outShapingPolicy:
            pg_spec.defaultPortConfig.outShapingPolicy = (vim.
                DVSTrafficShapingPolicy())
        _apply_dvportgroup_out_shaping(pg_name, pg_spec.defaultPortConfig.
            outShapingPolicy, pg_conf['out_shaping'])
    if 'security_policy' in pg_conf:
        if not pg_spec.defaultPortConfig.securityPolicy:
            pg_spec.defaultPortConfig.securityPolicy = vim.DVSSecurityPolicy()
        _apply_dvportgroup_security_policy(pg_name, pg_spec.
            defaultPortConfig.securityPolicy, pg_conf['security_policy'])
    if 'teaming' in pg_conf:
        if not pg_spec.defaultPortConfig.uplinkTeamingPolicy:
            pg_spec.defaultPortConfig.uplinkTeamingPolicy = (vim.
                VmwareUplinkPortTeamingPolicy())
        _apply_dvportgroup_teaming(pg_name, pg_spec.defaultPortConfig.
            uplinkTeamingPolicy, pg_conf['teaming'])