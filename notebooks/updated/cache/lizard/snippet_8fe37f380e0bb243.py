def list_by_claim(self, claim):
    if not isinstance(claim, QueueClaim):
        claim = self._claim_manager.get(claim)
    return claim.messages