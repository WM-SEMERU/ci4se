def get_sync_acl_cmds(self, switch_acls, expected_acls):
    switch_cmds = list()
    acls_to_delete = set(switch_acls.keys()) - set(expected_acls.keys())
    for acl in acls_to_delete:
        switch_cmds.append('no ip access-list %s' % acl)
    for acl, expected_rules in expected_acls.items():
        switch_rules = switch_acls.get(acl, set())
        rules_to_delete = switch_rules - expected_rules
        rules_to_add = expected_rules - switch_rules
        if acl in switch_acls and len(rules_to_add | rules_to_delete) == 0:
            continue
        switch_cmds.append('ip access-list %s dynamic' % acl)
        for rule in rules_to_delete:
            switch_cmds.append('no ' + rule)
        for rule in rules_to_add:
            switch_cmds.append(rule)
            switch_cmds.append('exit')
    return switch_cmds