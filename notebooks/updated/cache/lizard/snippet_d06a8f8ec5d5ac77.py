def _remove_till_caught_up_3pc(self, last_caught_up_3PC):
    outdated_pre_prepares = {}
    for key, pp in self.prePrepares.items():
        if compare_3PC_keys(key, last_caught_up_3PC) >= 0:
            outdated_pre_prepares[key] = pp
    for key, pp in self.sentPrePrepares.items():
        if compare_3PC_keys(key, last_caught_up_3PC) >= 0:
            outdated_pre_prepares[key] = pp
    self.logger.trace('{} going to remove messages for {} 3PC keys'.format(
        self, len(outdated_pre_prepares)))
    for key, pp in outdated_pre_prepares.items():
        self.batches.pop(key, None)
        self.sentPrePrepares.pop(key, None)
        self.prePrepares.pop(key, None)
        self.prepares.pop(key, None)
        self.commits.pop(key, None)
        self._discard_ordered_req_keys(pp)