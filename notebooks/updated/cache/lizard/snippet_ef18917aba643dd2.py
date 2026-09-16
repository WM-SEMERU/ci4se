def convert_fwdb_event_msg(self, rule, tenant_id, rule_id, policy_id):
    rule.update({'tenant_id': tenant_id, 'id': rule_id,
        'firewall_policy_id': policy_id})
    fw_rule_data = {'firewall_rule': rule}
    return fw_rule_data