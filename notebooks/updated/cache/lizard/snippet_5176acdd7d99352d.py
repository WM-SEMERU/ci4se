def should_stop(self, result):
    if result.get(DONE):
        return True
    for criteria, stop_value in self.stopping_criterion.items():
        if criteria not in result:
            raise TuneError('Stopping criteria {} not provided in result {}.'
                .format(criteria, result))
        if result[criteria] >= stop_value:
            return True
    return False