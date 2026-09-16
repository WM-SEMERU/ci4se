def execute_action(self, action_name, **options):
    assert action_name in NG_ACTIONS, 'wrong action - {0}'.format(action_name)
    action = NG_ACTIONS[action_name]
    self.loop.run_sync(lambda : action.execute(**options), timeout=self.timeout
        )