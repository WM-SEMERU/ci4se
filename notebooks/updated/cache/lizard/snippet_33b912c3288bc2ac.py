def _bytype(self, action_type, action_spec=None):
    for action in reversed(self.bill['actions']):
        if action_type in action['type']:
            for k, v in action_spec.items():
                if action[k] == v:
                    yield action