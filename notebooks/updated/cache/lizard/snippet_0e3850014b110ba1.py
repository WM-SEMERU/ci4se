def settle(self, transferred_amount: TokenAmount, locked_amount:
    TokenAmount, locksroot: Locksroot, partner_transferred_amount:
    TokenAmount, partner_locked_amount: TokenAmount, partner_locksroot:
    Locksroot, block_identifier: BlockSpecification):
    self.token_network.settle(channel_identifier=self.channel_identifier,
        transferred_amount=transferred_amount, locked_amount=locked_amount,
        locksroot=locksroot, partner=self.participant2,
        partner_transferred_amount=partner_transferred_amount,
        partner_locked_amount=partner_locked_amount, partner_locksroot=
        partner_locksroot, given_block_identifier=block_identifier)