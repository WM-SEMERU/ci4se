def notify_engine_activated(self, chain_head):
    chain_head_bytes = chain_head.SerializeToString()
    self._notify('consensus_notifier_notify_engine_activated',
        chain_head_bytes, len(chain_head_bytes))