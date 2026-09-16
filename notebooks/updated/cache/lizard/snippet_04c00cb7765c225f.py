def create_alert_policy(self, policy_name):
    policy_data = {'policy': {'incident_preference': 'PER_POLICY', 'name':
        policy_name}}
    create_policy = requests.post(
        'https://api.newrelic.com/v2/alerts_policies.json', headers=self.
        auth_header, data=json.dumps(policy_data))
    create_policy.raise_for_status()
    policy_id = create_policy.json()['policy']['id']
    self.refresh_all_alerts()
    return policy_id