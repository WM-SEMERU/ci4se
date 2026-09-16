def reset(self):
    if not self.chain_id:
        return
    saved, self.chain_id = self.chain_id, None
    try:
        self.call_no_reply(mitogen.core.Dispatcher.forget_chain, saved)
    finally:
        self.chain_id = saved