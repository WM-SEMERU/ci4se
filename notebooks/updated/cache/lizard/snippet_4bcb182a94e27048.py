def _process_zero_length(self, nozero, allow_arbitrary_shift):
    self.log('Called _process_zero_length')
    if not nozero:
        self.log('Processing zero length intervals not requested: returning')
        return
    self.log('Processing zero length intervals requested')
    self.log('  Checking and fixing...')
    duration = self.rconf[RuntimeConfiguration.ABA_NO_ZERO_DURATION]
    self.log(['  Requested no zero duration: %.3f', duration])
    if not allow_arbitrary_shift:
        self.log('  No arbitrary shift => taking max with mws')
        duration = self.rconf.mws.geq_multiple(duration)
    self.log(['  Actual no zero duration: %.3f', duration])
    max_index = len(self.smflist) - 1
    self.smflist.fix_zero_length_fragments(duration=duration, min_index=1,
        max_index=max_index)
    self.log('  Checking and fixing... done')
    if self.smflist.has_zero_length_fragments(1, max_index):
        self.log_warn(
            '  The fragment list still has fragments with zero length')
    else:
        self.log('  The fragment list does not have fragments with zero length'
            )