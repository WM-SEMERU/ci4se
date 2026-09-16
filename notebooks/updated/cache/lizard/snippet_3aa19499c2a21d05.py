def _val_from_env(self, env, attr):
    val = os.environ[env]
    if attr in ('rules', 'exclude_rules'):
        return self._rules_from_env(val)
    elif attr == 'priority':
        return dict(self._priority_from_env(val))
    elif attr in ('wait_command', 'history_limit', 'wait_slow_command',
        'num_close_matches'):
        return int(val)
    elif attr in ('require_confirmation', 'no_colors', 'debug',
        'alter_history', 'instant_mode'):
        return val.lower() == 'true'
    elif attr == 'slow_commands':
        return val.split(':')
    else:
        return val