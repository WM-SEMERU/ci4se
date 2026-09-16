def migrate_abci_chain(self):
    latest_chain = self.get_latest_abci_chain()
    if latest_chain is None:
        return
    block = self.get_latest_block()
    suffix = '-migrated-at-height-'
    chain_id = latest_chain['chain_id']
    block_height_str = str(block['height'])
    new_chain_id = chain_id.split(suffix)[0] + suffix + block_height_str
    self.store_abci_chain(block['height'] + 1, new_chain_id, False)