def _callback_new_block(self, latest_block: Dict):
    with self.event_poll_lock:
        latest_block_number = latest_block['number']
        confirmed_block_number = max(GENESIS_BLOCK_NUMBER, 
            latest_block_number - self.config['blockchain'][
            'confirmation_blocks'])
        confirmed_block = self.chain.client.web3.eth.getBlock(
            confirmed_block_number)
        for event in self.blockchain_events.poll_blockchain_events(
            confirmed_block_number):
            on_blockchain_event(self, event)
        state_change = Block(block_number=confirmed_block_number, gas_limit
            =confirmed_block['gasLimit'], block_hash=BlockHash(bytes(
            confirmed_block['hash'])))
        self.handle_and_track_state_change(state_change)