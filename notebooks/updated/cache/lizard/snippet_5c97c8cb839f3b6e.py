def update(self, alert_condition_id, policy_id, type=None, condition_scope=
    None, name=None, entities=None, metric=None, runbook_url=None, terms=
    None, user_defined=None, enabled=None):
    conditions_dict = self.list(policy_id)
    target_condition = None
    for condition in conditions_dict['conditions']:
        if int(condition['id']) == alert_condition_id:
            target_condition = condition
            break
    if target_condition is None:
        raise NoEntityException(
            'Target alert condition is not included in that policy.policy_id: {}, alert_condition_id {}'
            .format(policy_id, alert_condition_id))
    data = {'condition': {'type': type or target_condition['type'], 'name':
        name or target_condition['name'], 'entities': entities or
        target_condition['entities'], 'condition_scope': condition_scope or
        target_condition['condition_scope'], 'terms': terms or
        target_condition['terms'], 'metric': metric or target_condition[
        'metric'], 'runbook_url': runbook_url or target_condition[
        'runbook_url']}}
    if enabled is not None:
        data['condition']['enabled'] = str(enabled).lower()
    if data['condition']['metric'] == 'user_defined':
        if user_defined:
            data['condition']['user_defined'] = user_defined
        elif 'user_defined' in target_condition:
            data['condition']['user_defined'] = target_condition['user_defined'
                ]
        else:
            raise ConfigurationException(
                'Metric is set as user_defined but no user_defined config specified'
                )
    return self._put(url='{0}alerts_conditions/{1}.json'.format(self.URL,
        alert_condition_id), headers=self.headers, data=data)