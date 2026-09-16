def dequeue_pre_prepares(self):
    ppsReady = []
    for i, (pp, sender, reqIds) in enumerate(self.prePreparesPendingFinReqs):
        finalised = set()
        for r in reqIds:
            if self.requests.is_finalised(r):
                finalised.add(r)
        diff = reqIds.difference(finalised)
        if not diff:
            ppsReady.append(i)
        self.prePreparesPendingFinReqs[i] = pp, sender, diff
    for i in sorted(ppsReady, reverse=True):
        pp, sender, _ = self.prePreparesPendingFinReqs.pop(i)
        self.prePreparesPendingPrevPP[pp.viewNo, pp.ppSeqNo] = pp, sender
    r = 0
    while self.prePreparesPendingPrevPP and self.__is_next_pre_prepare(*
        self.prePreparesPendingPrevPP.iloc[0]):
        _, (pp, sender) = self.prePreparesPendingPrevPP.popitem(last=False)
        if not self.can_pp_seq_no_be_in_view(pp.viewNo, pp.ppSeqNo):
            self.discard(pp, 'Pre-Prepare from a previous view', self.
                logger.debug)
            continue
        self.logger.info('{} popping stashed PREPREPARE{} from sender {}'.
            format(self, pp, sender))
        self.process_three_phase_msg(pp, sender)
        r += 1
    return r