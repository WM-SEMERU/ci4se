def set_rule_enabled_state(self, enabled):
    data = {'ruleId': self.id, 'enabled': enabled}
    return self._restCall('rule/enableSimpleRule', json.dumps(data))