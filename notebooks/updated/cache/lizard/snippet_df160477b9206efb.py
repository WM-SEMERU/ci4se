def prepare(self):
    self.leader = False
    self.promises_received = set()
    self.nacks_received = set()
    self.proposal_id = ProposalID(self.highest_proposal_id.number + 1, self
        .network_uid)
    self.highest_proposal_id = self.proposal_id
    self.current_prepare_msg = Prepare(self.network_uid, self.proposal_id)
    return self.current_prepare_msg