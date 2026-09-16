def _process_stashed_pre_prepare_for_time_if_possible(self, key: Tuple[int,
    int]):
    self.logger.debug(
        '{} going to process stashed PRE-PREPAREs with incorrect times'.
        format(self))
    q = self.quorums.f
    if len(self.preparesWaitingForPrePrepare[key]) > q:
        times = [pr.ppTime for pr, _ in self.preparesWaitingForPrePrepare[key]]
        most_common_time, freq = mostCommonElement(times)
        if self.quorums.timestamp.is_reached(freq):
            self.logger.debug(
                '{} found sufficient PREPAREs for the PRE-PREPARE{}'.format
                (self, key))
            stashed_pp = self.pre_prepares_stashed_for_incorrect_time
            pp, sender, done = stashed_pp[key]
            if done:
                self.logger.debug('{} already processed PRE-PREPARE{}'.
                    format(self, key))
                return True
            stashed_pp[key] = pp, sender, True
            self.process_three_phase_msg(pp, sender)
            return True
    return False