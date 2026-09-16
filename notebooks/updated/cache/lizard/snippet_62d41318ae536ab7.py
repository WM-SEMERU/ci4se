def set_label(self, label):
    data = {'ruleId': self.id, 'label': label}
    return self._restCall('rule/setRuleLabel', json.dumps(data))