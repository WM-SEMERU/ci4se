def apply_policy(self, policy):
    tenant_name = policy['tenant_name']
    fw_id = policy['fw_id']
    fw_name = policy['fw_name']
    LOG.info(
        'asa_apply_policy: tenant=%(tenant)s fw_id=%(fw_id)s fw_name=%(fw_name)s'
        , {'tenant': tenant_name, 'fw_id': fw_id, 'fw_name': fw_name})
    cmds = ['conf t', 'changeto context ' + tenant_name]
    for rule_id, rule in policy['rules'].items():
        acl = self.build_acl(tenant_name, rule)
        LOG.info(
            'rule[%(rule_id)s]: name=%(name)s enabled=%(enabled)s protocol=%(protocol)s dport=%(dport)s sport=%(sport)s dip=%(dport)s sip=%(sip)s action=%(dip)s'
            , {'rule_id': rule_id, 'name': rule.get('name'), 'enabled':
            rule.get('enabled'), 'protocol': rule.get('protocol'), 'dport':
            rule.get('dst_port'), 'sport': rule.get('src_port'), 'dip':
            rule.get('destination_ip_address'), 'sip': rule.get(
            'source_ip_address'), 'action': rule.get('action')})
        if rule_id in self.rule_tbl:
            cmds.append('no ' + self.rule_tbl[rule_id])
        self.rule_tbl[rule_id] = acl
        if tenant_name in self.tenant_rule:
            if rule_id not in self.tenant_rule[tenant_name]['rule_lst']:
                self.tenant_rule[tenant_name]['rule_lst'].append(rule_id)
        cmds.append(acl)
    cmds.append('access-group ' + tenant_name + ' global')
    cmds.append('write memory')
    LOG.info('cmds sent is %s', cmds)
    data = {'commands': cmds}
    return self.rest_send_cli(data)