def add_policy(self, name, action, resource, subject, condition,
    policy_set_id=None, effect='PERMIT'):
    if not policy_set_id:
        policy_set_id = str(uuid.uuid4())
    if action not in ['GET', 'PUT', 'POST', 'DELETE']:
        raise ValueError('Invalid action')
    policy = {'name': name, 'target': {'resource': resource, 'subject':
        subject, 'action': action}, 'conditions': [{'name': '', 'condition':
        condition}], 'effect': effect}
    body = {'name': policy_set_id, 'policies': [policy]}
    result = self._put_policy_set(policy_set_id, body)
    return result