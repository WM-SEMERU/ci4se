def update_transfer(self, nonce: Nonce, balance_hash: BalanceHash,
    additional_hash: AdditionalHash, partner_signature: Signature,
    signature: Signature, block_identifier: BlockSpecification):
    self.token_network.update_transfer(channel_identifier=self.
        channel_identifier, partner=self.participant2, balance_hash=
        balance_hash, nonce=nonce, additional_hash=additional_hash,
        closing_signature=partner_signature, non_closing_signature=
        signature, given_block_identifier=block_identifier)