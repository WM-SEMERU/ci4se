def receive_accepted(self, msg):
    if self.final_value is not None:
        if (msg.proposal_id >= self.final_proposal_id and msg.
            proposal_value == self.final_value):
            self.final_acceptors.add(msg.from_uid)
        return Resolution(self.network_uid, self.final_value)
    last_pn = self.acceptors.get(msg.from_uid)
    if last_pn is not None and msg.proposal_id <= last_pn:
        return
    self.acceptors[msg.from_uid] = msg.proposal_id
    if last_pn is not None:
        proposal_key = str(last_pn)
        ps = self.proposals[proposal_key]
        ps.retain_count -= 1
        ps.acceptors.remove(msg.from_uid)
        if ps.retain_count == 0:
            del self.proposals[proposal_key]
    proposal_key = str(msg.proposal_id)
    if not proposal_key in self.proposals:
        self.proposals[proposal_key] = ProposalStatus(msg.proposal_value)
    ps = self.proposals[proposal_key]
    assert msg.proposal_value == ps.value, 'Value mismatch for single proposal!'
    ps.accept_count += 1
    ps.retain_count += 1
    ps.acceptors.add(msg.from_uid)
    if ps.accept_count == self.quorum_size:
        self.final_proposal_id = msg.proposal_id
        self.final_value = msg.proposal_value
        self.final_acceptors = ps.acceptors
        self.proposals = None
        self.acceptors = None
        return Resolution(self.network_uid, self.final_value)