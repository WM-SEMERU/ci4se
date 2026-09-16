def _check_restart_params(self, restart_strategy, min_beta, s_greedy,
    xi_restart):
    r
    if restart_strategy is None:
        return True
    if self.mode != 'regular':
        raise ValueError(
            'Restarting strategies can only be used with regular mode.')
    greedy_params_check = min_beta is None or s_greedy is None or s_greedy <= 1
    if restart_strategy == 'greedy' and greedy_params_check:
        raise ValueError(
            'You need a min_beta and an s_greedy > 1 for greedy restart.')
    if xi_restart is None or xi_restart >= 1:
        raise ValueError('You need a xi_restart < 1 for restart.')
    return True