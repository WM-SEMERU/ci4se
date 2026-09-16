def when_ends(self, timeformat='unix'):
    end_coverage = max([item.get_reference_time() for item in self._forecast])
    return timeformatutils.timeformat(end_coverage, timeformat)